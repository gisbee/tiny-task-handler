from os import getenv
from os.path import dirname, join

from dotenv import load_dotenv

env_file = join(dirname(__file__), ".env")
load_dotenv(env_file)


class Config(object):

    ENVIRONMENT = getenv("ENVIRONMENT")
    BASEDIR = dirname(__file__)

    # flask
    DEBUG = False
    CSRF_ENABLED = True
    TEMPLATES_AUTO_RELOAD = True
    PROPAGATE_EXCEPTIONS = True
    BUNDLE_ERRORS = True
    CORS_HEADERS = "Content-Type"
    SECRET_KEY = getenv("SECRET_KEY")

    # celery
    CELERY_BROKER_URL = getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = getenv("CELERY_RESULT_BACKEND")


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
