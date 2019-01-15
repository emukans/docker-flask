# Docker flask

The purpose of this project is to simplify the process of configuring Flask using Docker.
This docker setup contains the minimal configuration of Flask application.

## Getting started

1. Copy `.env.example` file to `.env`
    ```bash
    cp .env.example .env
    ```

2. Override environment variables in `.env` file

3. Start the project 
    ```bash
    docker-compose up -d
    ```

4. Visit http://localhost:8080/

## Useful commands
#### Get into container
```bash
docker-compose exec container_name bash

# E.g.
# To get into container with python and application
docker-compose exec app bash
```

#### Database

```bash
# In app container.

# View list of available commands
flask db

# Create migration for all new models.
flask db init

# Apply new migrations
flask db migrate
```

## Project description

Project contain 3 components:
* Nginx - to serve static files
* Gunicorn - as WSGI interface for python apps. 
* Flask app itself - contains all project business logic

## License

MIT License: see [the `LICENSE` file](https://github.com/emukans/docker-flask/blob/master/LICENSE).
