from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        print("Received data from Make.com:", data)
        # Yahan par aage hum video generation ka logic add karenge
        return jsonify({"status": "success", "message": "Video generation triggered!"}), 200
    return jsonify({"status": "active", "message": "Shayari Bot is running!"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
