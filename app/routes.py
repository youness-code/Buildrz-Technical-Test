from app import app
from flask import render_template, request, jsonify
from app import database as db

test=True

@app.route("/")
def homepage():
    db = None
    if test:
        items = {
            "id": 321,
            "parcelle": 9310000100234,
            "ca": 2000000,
            "cree-le": '2021-05-03',
            "status": 'en cours'
            }
    else:
        items = db.fetch_todo()
    return render_template("index.html", items=items)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new project """
    data = request.get_json()
    db.insert_new_project(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)