#API -http://127.0.0.1:5000/data
from flask import Flask ,jsonify

app=Flask(__name__)

data=[{"id":1,"Name":"Jay","age":24},{"id":2,"Name":"Aru","age":29},{"id":3,"Name":"sid","age":33}]

@app.route("/data",methods=["GET"])
def get_data():
    return jsonify(data)

@app.route("/data/<int:data_id>",methods=["GET"])
def get_data_id(data_id):
    for x in data:
        if x["id"] == data_id:
            return jsonify(x)
    return jsonify({"Error":"Data not available"}),404

if __name__=="__main__":
    app.run(debug=True)