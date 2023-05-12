from flask import Blueprint, render_template, abort, request, jsonify, Response
from jinja2 import TemplateNotFound
from database import Database
from utils import login_required


email_blueprint = Blueprint('email', __name__)



@email_blueprint.route('/emails', methods=['GET', 'POST'])
#@login_required
def email():
    if request.method == 'GET':
        response = Database().find()
        del response['_id']
        return jsonify(response)

    if request.method == 'POST':
        print("rtg")
        data = request.get_json()
        print(data, type(data))
        return data