import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from labs.lab1_image_ops import process_lab1

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("static", "uploads")
OUTPUT_FOLDER = os.path.join("static", "outputs")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ── Lab Registry ──────────────────────────────────────────────
# Add each new lab here as you complete it throughout the semester.
# The navbar is built dynamically from this list, so a new lab
# only needs: (1) an entry here, (2) a route below, (3) an HTML template.
LABS = [
    {"id": "lab1", "label": "Lab 1: Image Manipulation"},
    # {"id": "lab2", "label": "Lab 2: ..."},
    # {"id": "lab3", "label": "Lab 3: ..."},
]


@app.context_processor
def inject_labs():
    """Make the lab list available to every template automatically."""
    return {"labs": LABS}


# ── Routes ────────────────────────────────────────────────────

@app.route("/")
def index():
    return redirect(url_for("lab1"))


@app.route("/lab1", methods=["GET", "POST"])
def lab1():
    results = None
    error = None

    if request.method == "POST":
        file = request.files.get("image")
        coord_x = request.form.get("coord_x", 50)
        coord_y = request.form.get("coord_y", 50)
        scale_percent = request.form.get("scale_percent", 50)

        if not file or file.filename == "":
            error = "Please upload a valid image file."
        else:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            try:
                results = process_lab1(
                    filepath, OUTPUT_FOLDER, coord_x, coord_y, scale_percent
                )
            except Exception as e:
                error = str(e)

    return render_template("lab1.html", active_lab="lab1", results=results, error=error)


# ── Add future lab routes below this line ─────────────────────
# @app.route("/lab2", methods=["GET", "POST"])
# def lab2():
#     ...


if __name__ == "__main__":
    app.run(debug=True)
