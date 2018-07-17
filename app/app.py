from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.debug import DebuggedApplication


app = Flask(__name__, instance_relative_config=True)

# start with a default configuration
app.config.from_object('config')

# To override default config, create new config file in `app/instance/local_config.py`
app.config.from_pyfile('local_config.py')

if app.debug:
    app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import views
import models
