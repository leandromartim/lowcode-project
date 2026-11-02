
from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)
app.secret_key = 'development_secret_key'  # Required for flashing or general app security

# Simple standard library regex for email validation
EMAIL_REGEX = re.compile(r"^[\w\.-]+@([\w-]+\.)+[\w-]{2,4}$")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    errors = {}
    name = ''
    email = ''
    message = ''

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Server-side validation
        if not name:
            errors['name'] = 'Name cannot be empty.'

        if not email:
            errors['email'] = 'Email cannot be empty.'
        elif not EMAIL_REGEX.match(email):
            errors['email'] = 'Please enter a valid email address.'

        if not message:
            errors['message'] = 'Message cannot be empty.'

        # If there are validation errors, re-render the form with error messages and retained input
        if errors:
            return render_template('contact.html', errors=errors, name=name, email=email, message=message)

        # Successful submission (no data storage required)
        return redirect(url_for('contact_success'))

    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return render_template('contact_success.html')

if __name__ == '__main__':
    app.run(debug=True)
