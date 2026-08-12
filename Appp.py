from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>VIDEX Trading AI</title>
        <style>
            body {
                background: #111;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 80px;
            }

            h1 {
                font-size: 35px;
            }

            .status {
                background: #222;
                padding: 20px;
                margin: 20px auto;
                max-width: 400px;
                border-radius: 15px;
            }

            .online {
                color: #00ff88;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <h1>VIDEX TRADING AI</h1>

        <div class="status">
            <h2>System Status</h2>
            <p class="online">● ONLINE</p>
            <p>AI Engine: READY</p>
            <p>Market Analysis: READY</p>
        </div>

        <p>Welcome to VIDEX Trading AI 🚀</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
