# CSST 106 — Perception & Computer Vision  
## Laboratory Portfolio Web Application

A single unified Flask web application that houses **all** CSST 106 laboratory activities. Each lab is accessible via its own labeled tab in the navigation bar. The instructor can upload images/videos, run the computer vision processing, and view outputs directly in the browser.

---

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the web application
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

---

## Project Structure

```
CSST106-Computer-Vision-Labs/
├── app.py                      # Main Flask app, routes & lab registry
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── labs/                       # Processing logic for each lab
│   ├── __init__.py
│   └── lab1_image_ops.py       # Lab 1 — Image Representation & Manipulation
├── templates/                  # Jinja2 HTML templates
│   ├── base.html               # Shared layout with dynamic lab nav tabs
│   └── lab1.html               # Lab 1 interactive UI & output display
└── static/
    ├── css/
    │   └── style.css           # Custom pink glassmorphism theme
    ├── uploads/                # Uploaded input images
    └── outputs/                # Processed output images
```

---

## Adding a New Lab

1. Create `labs/labN_<name>.py` with the processing function.  
2. Create `templates/labN.html` extending `base.html`.  
3. In `app.py`: import the function, add an entry to `LABS`, and add a route.

---

## Module Index

| Lab | Title | Route | Status |
|-----|-------|-------|--------|
| 1 | Introduction to Computer Vision & Image Manipulation | `/lab1` | ✅ Complete |
| 2 | _TBD_ | `/lab2` | 🔲 Pending |
| 3 | _TBD_ | `/lab3` | 🔲 Pending |
