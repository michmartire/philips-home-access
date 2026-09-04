from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Philips NFC bridge is running"
    })

@app.route("/unlock")
def unlock():
    return jsonify({
        "status": "disabled",
        "message": "Unlock is not configured yet"
    }), 403
