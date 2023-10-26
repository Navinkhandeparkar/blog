import os

class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Using SQLite for simplicity


class DevelopmentConfig(Config):
    # development config
    pass

class TestingConfig(Config):
    # testing config
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class ProductionConfig(Config):
    # production config
    pass