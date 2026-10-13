import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v2")


def add(a, b):
    return a + b


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Week 09 Application",
        "version": APP_VERSION,
        "message": "Application is running successfully!"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy", "version": APP_VERSION})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

