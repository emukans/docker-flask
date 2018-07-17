import os
import uuid

DEBUG = False
TESTING = False
DEVELOPMENT = False

# if you don't override the secret key, one will be chosen for you
SECRET_KEY = uuid.uuid4().hex

DATABASE_URL = 'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}'.format(db_user=os.environ.get('DB_USER'), db_password=os.environ.get('DB_PASSWORD'),
                                                                                      db_host=os.environ.get('DB_HOST'), db_name=os.environ.get('DB_NAME'))
SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False
