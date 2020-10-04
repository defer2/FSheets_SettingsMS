from database import db
from models import Settings, SettingsSchema


def hello_world():
    return 'Hello World!'


def get_settings():
    return SettingsSchema(many=True).dump(Settings.query.all())


def update_settings(settings):
    try:
        api_timesheets_url = settings['API_TIMESHEETS_URL']
        api_projects_url = settings['API_PROJECTS_URL']
        api_tasks_url = settings['API_TASKS_URL']
        api_clarityppm_url = settings['API_CLARITYPPM_URL']
        ppm_url = settings['PPM_URL']
        ppm_username = settings['PPM_USERNAME']
        ppm_password = settings['PPM_PASSWORD']

        one_setting = db.session.query(Settings).filter_by(id=1).one()

        one_setting.API_TIMESHEETS_URL = api_timesheets_url or one_setting.API_TIMESHEETS_URL
        one_setting.API_PROJECTS_URL = api_projects_url or one_setting.API_PROJECTS_URL
        one_setting.API_TASKS_URL = api_tasks_url or one_setting.API_TASKS_URL
        one_setting.API_CLARITYPPM_URL = api_clarityppm_url or one_setting.API_CLARITYPPM_URL
        one_setting.PPM_URL = ppm_url or one_setting.PPM_URL
        one_setting.PPM_USERNAME = ppm_username or one_setting.PPM_USERNAME
        one_setting.PPM_PASSWORD = ppm_password or one_setting.PPM_PASSWORD

        db.session.commit()
        result = {
            "error": False,
            "message": "OK"
        }
    except Exception as e:
        result = {
            "error": True,
            "message": str(e)
        }
    finally:
        return result
