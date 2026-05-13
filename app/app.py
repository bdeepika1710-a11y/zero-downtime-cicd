from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1")

@app.route("/")
def home():
    return f"""
    <html>
    <head>
        <title>Zero Downtime CI/CD</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 80px;">
        <h1>Zero Downtime CI/CD Pipeline - Updated Version</h1>
        <h2>Application Version: {VERSION}</h2>
        <p>Status: Updated Version Running Successfully</p>
        <p>Deployed using Docker, GitHub Actions, AWS EC2 and Nginx</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy", "version": VERSION}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
