from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# start with a default configuration
app.config.from_object('config')

# To override default config, create new config file in `app/instance/local_config.py`
app.config.from_pyfile('local_config.py')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import views
