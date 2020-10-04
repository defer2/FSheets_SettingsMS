from flask import Blueprint, jsonify, request, abort, Response
from flask_cors import cross_origin
import controllers
from models import Settings, SettingsSchema

view_blueprint = Blueprint('view_blueprint', __name__)


@view_blueprint.route('/', methods=['GET'])
@cross_origin()
def hello_world():
    return controllers.hello_world()


@view_blueprint.route('/view', methods=['GET'])
@cross_origin()
def get_settings():
    return jsonify(controllers.get_settings())


@view_blueprint.route('/', methods=['PUT'])
@cross_origin()
def update_settings():
    settings = request.json
    result = controllers.update_settings(settings)
    if result['error']:
        abort(Response(result['message'], 403))
    else:
        return result['message']