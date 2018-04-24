import os


class Config(object):
    IN_PRODUCTION = os.getenv('thisisourproductionvar', False)

    SECRET_KEY = os.getenv("SECRET_KEY")

    PREDICT_HOST = os.getenv("PREDICT_HOST")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///:memory:")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ERROR_404_HELP = False

    KONCH_SHELL = 'ipy'

    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(name)s:%(lineno)s %(message)s'
            },
        },
        'handlers': {
            'local': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
            },
        },
        'loggers': {
            'app': {
                'level': 'INFO' if IN_PRODUCTION else 'DEBUG',
            }
        },
    }
