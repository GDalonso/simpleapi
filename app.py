from flask import request, redirect, session, url_for

from Database import dbinsertusuario, removepost
from models import User


# Configura a aplicação, os diretorios de CSS, JS, Imagens e fontes
# app = Flask(__name__, template_folder='templates', static_folder='static')
# Define uma chave para o HEROKU
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'WYZ')

# GZIP - Utilizado para compactar a pagina
# gzip = Compress(app)


@app.route("/criarusuario", methods=["POST"])
def createuser():
    """
    Create a User with the create user form contents
    """

    # Form contents
    nomeusuario = request.form["nomeusuario"]
    senha = request.form["senha"]
    nomedisplay = request.form["nomedisplay"]
    usuario = User(nomeusuario, nomedisplay, senha)

    # Insert the object converted to dict in the database
    dbinsertusuario(usuario.__dict__)

    # Dynamic route to the index function
    return redirect(url_for("index"))
