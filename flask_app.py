from flask import Flask, jsonify

from database import dbinsertusuario, dbretrieveusers, dbremoveuser
from models import User

# from flask_talisman import Talisman

app = Flask(__name__)
app.secret_key = "dalonso"
# Talisman(app)

# Configura a aplicação, os diretorios de CSS, JS, Imagens e fontes
# app = Flask(__name__, template_folder='templates', static_folder='static')
# Define uma chave para o HEROKU
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'WYZ')

# GZIP - Utilizado para compactar a pagina
# gzip = Compress(app)


@app.route("/")
def inicial():
    return "tá funcionando o animal"

@app.route("/newUser", methods=["POST"])
def new_user():
    """
    Create a User with the create user form contents
    """
    from flask_restful import reqparse

    parser = reqparse.RequestParser()

    parser.add_argument("firstname", type=str, help="person's first name")
    parser.add_argument("lastname", type=str, help="person's lastname name")
    parser.add_argument("fromEmail", type=str, help="person's fromEmail")
    parser.add_argument("games", type=list, help="list of games the person plays")
    parser.add_argument(
        "onlineHour",
        type=str,
        help="devia ser uma data essa porra, mas o cliente mandou por string",
    )
    parser.add_argument("nickname", type=str, help="person's nickname")

    args = parser.parse_args()

    # Form contents
    firstname = args["firstname"]
    lastname = args["lastname"]
    fromEmail = args["fromEmail"]
    games = args["games"]
    onlineHour = args["onlineHour"]
    nickname = args["nickname"]

    usuario = User(firstname, lastname, fromEmail, games, onlineHour, nickname)

    # Insert the object converted to dict in the database
    dbinsertusuario(usuario.__dict__)

    # Dynamic route to the index function
    return {200: "deu certo"}


@app.route("/listUsers")
def list_users():
    """
    List all users in the database
    """
    return jsonify(dbretrieveusers())


# todo trocar essa rota pra delete ao invés de get
@app.route("/deleteUser/<_userid>")
def delete_user(_userid: str):
    """
    delete user with the given id from the database
    :param _userid: Id of a user to be removed from database
    """
    result = dbremoveuser(_userid)
    if "ok" in result.keys():
        return {200: "removed"}
    return {500: "not removed"}

if __name__ == "__main__":
    app.run(port=800)
