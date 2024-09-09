from flask import Flask
from flask_restful import Api

from resources.IndexResource import IndexResource
from resources.UsuariosResource import UsuariosResource, UsuarioResource

# Cors
# Blueprint
# Marshal
# Database

app = Flask(__name__)
api = Api(app)


api.add_resource(IndexResource, '/')
api.add_resource(UsuariosResource, '/usuarios')
api.add_resource(UsuarioResource, '/usuarios/<string:usuario_id>')

if __name__ == '__main__':
    app.run(debug=True)
