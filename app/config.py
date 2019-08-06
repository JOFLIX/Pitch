import os
# from . import app
class Config:
    '''
    General configuration parent class
    '''

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SECRET_KEY = "b'\xfd\x1c]@g*\xe3\x92\x8c\xa1\x93\xbb\xe3\x84\x9a\x8f\xe2\xf2\x7f\x86\x18oVM'"
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:123@localhost/pitches'

    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Pruduction  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''


class TestConfig(Config):
    '''
    For tests
    '''


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:123@localhost/pitches'


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")