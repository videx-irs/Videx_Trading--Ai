from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>VIDEX</h1>
    <p>Welcome to VIDEX Social App 🚀</p>
    <p>Status: ONLINE</p>
    """

@app.route("/api/status")
def status():
    return jsonify({
        "app": "VIDEX",
        "status": "online",
        "version": "1.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
