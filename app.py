import os.path
from flask import Flask
from database import db
from views import view_blueprint
from flask_cors import CORS


def create_app():
    app_settings = Flask(__name__)
    app_settings.config['DEBUG'] = True
    app_settings.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/settings.db'
    app_settings.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_settings.config['CORS_HEADERS'] = 'Content-Type'

    db.init_app(app_settings)
    app_settings.register_blueprint(view_blueprint, url_prefix='')
    return app_settings


def setup_database(app_settings):
    with app_settings.app_context():
        db.create_all()


app = create_app()
cors = CORS(app)

if __name__ == '__main__':
    if not os.path.isfile('database/settings.db'):
        setup_database(app)

    app.run(host='192.168.0.50', port=5014)

