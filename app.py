
import re

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Email validation
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


# Original Week 1 route
@app.route("/")
def home():
    return "<h1>Hello from Leandro</h1>"


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
