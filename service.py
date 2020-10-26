import flask
from flask import request
from flask import Response

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/register', methods=['POST'])
def register():
   return Response("CREATED", status=201, mimetype='application/json')

@app.route('/changePassword', methods=['POST'])
def change():
   return Response("CREATED", status=201, mimetype='application/json')

@app.route('/login', methods=['GET'])
def login():
   return Response("OK", status=200, mimetype='application/json')

app.run(host='0.0.0.0')
