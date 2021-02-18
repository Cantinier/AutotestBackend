from app import app
from flask import request
from app import sqllib


@app.route('/login', methods=['POST'])
def login():
    print("login")
    username = request.json["login"]
    password = request.json["password"]
    result = sqllib.login(username, password)
    return result


@app.route('/registration', methods=['POST'])
def registration():
    username = request.json["login"]
    password = request.json["password"]
    front_name = request.json["front_name"]
    result = sqllib.reg(username, password, front_name)
    return result
