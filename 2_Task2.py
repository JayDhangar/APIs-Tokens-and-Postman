# I have launched this FlaskAPP and then POST- http://127.0.0.1:5000/post in body section I have written raw Json data{ "name":"jay","age":24} and posted it
from flask import Flask, request ,jsonify

app=Flask(__name__)

@app.route("/post",methods=["POST"])
def received():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error":"no json body found"})
    return jsonify({"received":data}),200

if __name__ == "__main__":
    app.run(debug=True)