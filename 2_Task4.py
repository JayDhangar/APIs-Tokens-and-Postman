#http://127.0.0.1:8000/secure  In headers key:Authorization and value:Bearer 1234@Hello
from flask import Flask, request, jsonify

app = Flask(__name__)
Token = "1234@Hello"

@app.route("/secure",methods=["GET"])
def secure():
    key = request.headers.get("Authorization")

    if key == f"Bearer {Token}":
        return jsonify({"send": "Access Granted"})
    return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True,port=8000)
