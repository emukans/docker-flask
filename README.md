#Docker flask

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

4. Open [localhost](http://localhost:8000/) `http://localhost:8000/`

## Project description

Project contain 3 components:
* Nginx - to serve static files
* Gunicorn - as WSGI interface for python apps. 
* Flask app itself - contains all project business logic

## License

MIT License: see [the `LICENSE` file](https://github.com/emukans/docker-flask/blob/master/LICENSE).
