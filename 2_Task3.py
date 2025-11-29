#http://127.0.0.1:6000/test/human     I have tested Post,Put,Get,Delete on postman

from flask import Flask, request, jsonify

app = Flask(__name__)
data = {}

@app.route("/test/<key>", methods=["POST"])
def create_test(key):

    data[key] = request.json["value"]
    return jsonify({"item":key,"value": data[key]})

@app.route("/test/<key>", methods=["PUT"])
def update_item(key):
    data[key] = request.get_json(silent=True)["value"]
    return jsonify({"Item":data[key],"status":"updated"})

@app.route("/test/<key>", methods=["GET"])
def get_item(key):
    return jsonify({key: data.get(key)}),200

@app.route("/test/<key>", methods=["DELETE"])
def delete_item(key):
    data.pop(key, None)
    return jsonify({"Item":key,"status": "deleted"})

if __name__ == "__main__":
    app.run(debug=True,port=6000)
