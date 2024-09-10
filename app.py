from flask import Flask
from helpers.api import api, blueprint
from helpers.cors import cors
from resources.IndexResource import IndexResource
from resources.UsuariosResource import UsuariosResource, UsuarioResource

# Cors
# Blueprint
# Marshal
# Database

app = Flask(__name__)
api.__init__(app)
cors.__init__(app)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)
