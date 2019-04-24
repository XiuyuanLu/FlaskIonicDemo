from flask import Flask
from flask import request
from flask_cors import CORS
from database import db_session
from database import init_db
from models import User

app = Flask(__name__)
CORS(app, supports_credentials=True)
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login',methods=["GET","POST"])
def login():

    username = request.args.get("username")
    password = request.args.get("password")

    if validate(username, password) is True:
        return "{\"login_status\":\"success\"}"
    else:
        return "{\"login_status\":\"fail\"}"

def validate(username, password):
    return username == "xiuyuan" and password == "liveordie2011"

if __name__ == '__main__':
    app.run()

@app.route('/insertDB')
def insertDB():
    admin_user = User('guest','guest')
    db_session.add(admin_user)
    db_session.commit()
    return "added"
