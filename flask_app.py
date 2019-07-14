# A very simple Flask Hello World app for you to get started with...

from flask import Flask, jsonify
from database import dbinsertUser, dbretrieveUsers, dbremoveUser
from models import User


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello from Flask!"


@app.route("/listUsers")
def list_users():
    """
    List all users in the database
    """
    return jsonify(dbretrieveUsers())


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

    user = User(firstname, lastname, fromEmail, games, onlineHour, nickname)

    # Insert the object converted to dict in the database
    result = dbinsertUser(user.__dict__)

    # Dynamic route to the index function
    return (
        jsonify({200: "Inserted"})
        if "error" not in result.keys()
        else jsonify({500: result["error"]})
    )


@app.route("/deleteUser/<_userid>", methods=["DELETE"])
def delete_user(_userid: str):
    """
    delete user with the given id from the database
    :param _userid: Id of a user to be removed from database
    """
    result = dbremoveUser(_userid)
    if "ok" in result.keys():
        return jsonify({200: "Removed"})
    return jsonify({500: "Not Removed"})
