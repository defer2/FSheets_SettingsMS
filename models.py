from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from database import db


class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    API_TASKS_URL = db.Column(db.String(250))
    API_PROJECTS_URL = db.Column(db.String(250))
    API_TIMESHEETS_URL = db.Column(db.String(250))
    API_CLARITYPPM_URL = db.Column(db.String(250))
    PPM_URL = db.Column(db.String(250))
    PPM_USERNAME = db.Column(db.String(250))
    PPM_PASSWORD = db.Column(db.String(250))


class SettingsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Settings
        load_instance = True
