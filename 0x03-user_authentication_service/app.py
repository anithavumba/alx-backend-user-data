#!/usr/bin/env python3
"""
Flask app
"""
import uuid
from flask import (
    Flask,
    request,
    jsonify,
    abort,
    redirect,
    url_for
)

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Return json response
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    """
    Register new users
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": f"{email}", "message": "user created"})

# Rest of your route handlers go here
users = {
    "bob@bob.com": "mySuperPwd"
}

@app.route('/sessions', methods=['POST'])
def login():
    if not request.form or 'email' not in request.form or 'password' not in request.form:
        abort(400)  # Bad request

    email = request.form['email']
    password = request.form['password']

    if email not in users or users[email] != password:
        abort(401)  # Unauthorized

    # Successful login
    session_id = str(uuid.uuid4())  # Generate a unique session ID
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)

    return response

if __name__ == '__main__':
    app.run(debug=True)
