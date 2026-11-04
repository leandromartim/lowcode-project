import re
import sqlite3
from datetime import date
from pathlib import Path

from flask import Flask, abort, g, redirect, render_template, request, url_for

app = Flask(__name__)

# SQLite database lives in Flask's instance folder (not committed to git)
DATABASE = Path(app.instance_path) / "solomind.db"

STATUSES = ("todo", "in_progress", "done")
STATUS_LABELS = {
    "todo": "To do",
    "in_progress": "In progress",
    "done": "Done",
}
MAX_TITLE_LENGTH = 200

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL CHECK (length(title) <= 200),
    description TEXT,
    status TEXT NOT NULL DEFAULT 'todo'
        CHECK (status IN ('todo', 'in_progress', 'done')),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    due_date DATE
);
"""

# Email validation
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


# ---------- Database helpers ----------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    DATABASE.parent.mkdir(parents=True, exist_ok=True)
    db = get_db()
    db.executescript(SCHEMA)
    db.commit()


with app.app_context():
    init_db()


@app.context_processor
def inject_status_labels():
    return {"STATUS_LABELS": STATUS_LABELS, "STATUSES": STATUSES}


# ---------- Task routes ----------

@app.route("/")
def task_list():
    db = get_db()
    tasks = db.execute(
        "SELECT id, title, status, due_date, created_at "
        "FROM tasks ORDER BY created_at DESC, id DESC"
    ).fetchall()
    return render_template("index.html", tasks=tasks)


@app.route("/task/new")
def task_new():
    return render_template("task_new.html", errors={}, form={})


def validate_task(title, due_date):
    errors = {}

    if not title:
        errors["title"] = "Please enter a title."
    elif len(title) > MAX_TITLE_LENGTH:
        errors["title"] = f"Title must be {MAX_TITLE_LENGTH} characters or fewer."

    if due_date:
        try:
            date.fromisoformat(due_date)
        except ValueError:
            errors["due_date"] = "Please enter a valid date."

    return errors


@app.route("/task", methods=["POST"])
def task_create():
    title = request.form.get("title", "").strip()
    description = request.form.get("description", "").strip()
    due_date = request.form.get("due_date", "").strip()

    errors = validate_task(title, due_date)

    if errors:
        return (
            render_template(
                "task_new.html",
                errors=errors,
                form={
                    "title": title,
                    "description": description,
                    "due_date": due_date,
                },
            ),
            400,
        )

    db = get_db()
    db.execute(
        "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
        (
            title,
            description or None,
            date.fromisoformat(due_date).isoformat() if due_date else None,
        ),
    )
    db.commit()
    return redirect(url_for("task_list"))


def get_task_or_404(task_id):
    task = get_db().execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    if task is None:
        abort(404)
    return task


@app.route("/task/<int:task_id>")
def task_detail(task_id):
    task = get_task_or_404(task_id)
    return render_template("task_detail.html", task=task)


@app.route("/task/<int:task_id>/status", methods=["POST"])
def task_update_status(task_id):
    get_task_or_404(task_id)

    status = request.form.get("status", "")
    if status not in STATUSES:
        abort(400)

    db = get_db()
    db.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    db.commit()
    return redirect(url_for("task_detail", task_id=task_id))


# ---------- Existing Week 2 contact form (unchanged) ----------

# Contact form validation
def validate_contact(name, email, message):
    errors = {}

    if not name:
        errors["name"] = "Please enter your name."

    if not email:
        errors["email"] = "Please enter your email address."
    elif len(email) > 254 or not EMAIL_RE.match(email):
        errors["email"] = "Please enter a valid email address."

    if not message:
        errors["message"] = "Please enter a message."

    return errors


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        errors = validate_contact(name, email, message)

        if errors:
            return (
                render_template(
                    "contact.html",
                    errors=errors,
                    form={"name": name, "email": email, "message": message},
                ),
                400,
            )

        # No data is stored or sent yet.
        return redirect(url_for("contact_thanks"))

    return render_template("contact.html", errors={}, form={})


@app.route("/contact/thanks")
def contact_thanks():
    return render_template("contact_thanks.html")


if __name__ == "__main__":
    app.run(debug=True)
