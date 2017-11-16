import os

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = os.urandom(24) or os.environ['SECRET_KEY']
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    OAUTH_CREDENTIALS = {
        'spotify': {
            'id': os.environ.get('SPOTIFY_CLIENT_ID'),
            'secret': os.environ.get('SPOTIFY_CLIENT_SECRET'),
        }
    }

    @staticmethod
    def init_app(app):
        pass
