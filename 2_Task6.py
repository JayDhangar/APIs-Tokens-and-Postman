from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/square", methods=["POST"])
def square():
    num = request.json["num"]
    return jsonify({"square": num * num})

if __name__ == "__main__":
    app.run(debug=True)
