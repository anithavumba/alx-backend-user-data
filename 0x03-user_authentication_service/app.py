#!/usr/bin/env python3

"""
Flask app
"""
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

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def create_token(user_id):
    s = Serializer("mysecretkey", 3600)
    token = s.dumps({"user_id": user_id}).decode("utf-8")
    return token

@app.route("/", methods=["GET"], strict_slashes=False)
def index() -> str:
    """
    Return json respomse
    {"message": "Bienvenue"}
    """
    return jsonify({"message": "Bienvenue"})

# Rest of your route definitions...

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
