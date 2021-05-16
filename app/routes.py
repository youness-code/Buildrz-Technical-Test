from app import app
from flask import Flask, render_template, request, jsonify
from app import database as db

app = Flask(__name__)

projets = [
    {
        'id': '321',
        'parcelle': '9310000100234',
        'ca': '2000000',
        'cree_le': '2021-05-03',
        'status': 'en cours'
    }
]

test = True

@app.route("/projets", methods=['GET'])
def mes_projets():
    if test: 
        return jsonify({'Mes projets':projets})
    
    

@app.route("/projets/?code_postal=93100&statut=en+cours", methods=['GET'])
def homepage():
    items = db.fetch_todo()
    return render_template("index.html", items=items)


@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new project """
    data = request.get_json()
    db.insert_new_project(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)
