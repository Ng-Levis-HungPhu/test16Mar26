from flask import Flask, request, jsonify
from flask_cors import CORS
import webbrowser

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "<h1>Server đang chạy 🚀</h1>"

# API GET
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Python backend 🐍"})

# API POST
@app.route("/api/data", methods=["POST"])
def data():
    content = request.json
    name = content.get("name")
    return jsonify({"message": f"Hello {name}"})


if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    app.run(debug=True)