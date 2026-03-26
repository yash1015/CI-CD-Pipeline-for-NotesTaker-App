from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

NOTES_FILE = "notes.json"


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


@app.route("/")
def index():
    notes = load_notes()
    notes.sort(key=lambda x: x["created_at"], reverse=True)
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add_note():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()
    color = request.form.get("color", "#ffffff")

    if title or content:
        notes = load_notes()
        note = {
            "id": int(datetime.now().timestamp() * 1000),
            "title": title or "Untitled",
            "content": content,
            "color": color,
            "created_at": datetime.now().isoformat(),
        }
        notes.append(note)
        save_notes(notes)

    return redirect(url_for("index"))


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete_note(note_id):
    notes = load_notes()
    notes = [n for n in notes if n["id"] != note_id]
    save_notes(notes)
    return redirect(url_for("index"))


@app.route("/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note(note_id):
    notes = load_notes()
    note = next((n for n in notes if n["id"] == note_id), None)
    if not note:
        return redirect(url_for("index"))

    if request.method == "POST":
        note["title"] = request.form.get("title", "").strip() or "Untitled"
        note["content"] = request.form.get("content", "").strip()
        note["color"] = request.form.get("color", "#ffffff")
        save_notes(notes)
        return redirect(url_for("index"))

    return render_template("edit.html", note=note)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
