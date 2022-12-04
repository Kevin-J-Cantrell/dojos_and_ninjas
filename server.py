from flask_app import app
from flask_app.controller import dojosController
from flask_app.controller import ninjasController
from flask_app.models import ninjas
from flask_app.models import dojos

if __name__ == '__main__':
    app.run(debug=True, port=8000)