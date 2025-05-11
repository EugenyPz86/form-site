from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbygHBp5bgLh6VWLVmrsxiYtThMtaeEv75eK1yjVJm7RXzS8M23qII2WWM7Xvz-tu55IGg/exec"  # ← сюда вставь свой скрипт

@app.route("/", methods=["POST"])
def proxy():
    data = request.json
    try:
        response = requests.post(GOOGLE_SCRIPT_URL, json=data)
        return jsonify({"status": "ok", "google_status": response.status_code}), response.status_code
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500