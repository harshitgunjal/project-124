from flask import Flask, jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'mobilephone',
        'description': u'',
        'done':False
    },
    {
        'id':2,
        'title':u'landlinephones',
        'description':u'',
        'done':False
    }
]

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":" please provide the data"
        },400)
    task={
        'id':tasks[-1]["id"]+1,
        'title':request.json['name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
            "status":"sucess",
            "message":"task added sucessfuly"
        })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks
    })
    
if(__name__ == "__main__"):
    app.run(debug=True)

