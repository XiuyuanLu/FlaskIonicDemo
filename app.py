from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=["GET","POST"])
def login():

    username = request.args.get("username")
    password = request.args.get("password")

    print(username=="xiuyuan")
    print(validate(username,password))

    if validate(username, password) is True:
        return "{\"login_status\":\"success\"}"
    else:
        return "{\"login_status\":\"fail\"}"

def validate(username, password):
    return username == "xiuyuan" and password == "liveordie2011"

if __name__ == '__main__':
    app.run()
