from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>VIDEX</title>
        </head>
        <body>
            <h1>VIDEX</h1>
            <p>Welcome to VIDEX Social App 🚀</p>
            <p>Status: ONLINE</p>
        </body>
    </html>
    """

@app.route("/api/status")
def status():
    return jsonify({
        "app": "VIDEX",
        "status": "online",
        "version": "1.0"
    })
