from flask import Flask, request, jsonify
from user_service import *

app = Flask(__name__)

@app.route('/add-user')
def add_user():
    user = dict()
    for key, val in request.args.items():
        user[key] = val

    return response(save_user(user))


@app.route('/delete-user/<id>')
def del_user(id):
    return response(delete_user(id))


def response(e):
    resp = {'status': e[0], 'msg': e[1]}
    return jsonify(resp), 200 if e[0] else 201


if __name__ == '__main__':
    app.run(debug = True)

