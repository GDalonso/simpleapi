from bson.objectid import ObjectId
from pymongo import MongoClient
from typing import Dict


def connectDB(coll="sheplaysCadastros"):
    try:
        # Create the auth client in mlab
        client = MongoClient(
            "mongodb://adminsheplays:Jp4W7e9CzUR3wKP@ds349857.mlab.com:49857/sheplays"
        )
        # Select the database we want to use
        db = client.sheplays
        # Return the desired collection
        if coll == "sheplaysCadastros":
            return db.cadastros
    except Exception as e:
        return {"error": "Error trying to connect to database"}


def dbinsertUser(usertoinsert):
    try:
        collection = connectDB("sheplaysCadastros")
        if isinstance(collection, Dict) and "error" in collection.keys():
            return collection
        # insert the document in the collection and returns the given id
        doc_id = collection.insert_one(usertoinsert).inserted_id
    except Exception as e:
        return {"error": "error writing to database"}


def dbretrieveUser(user):
    try:
        collection = connectDB("sheplaysCadastros")
        if isinstance(collection, Dict) and "error" in collection.keys():
            return collection
        user = collection.find_one({"username": user})
        return user
    except:
        return {"error": "error retrieving user from database"}


def dbretrieveUsers():
    try:
        collection = connectDB("sheplaysCadastros")
        if isinstance(collection, Dict) and "error" in collection.keys():
            return collection

        dict_users = {}
        # retrieve all users without their password hashes
        for user in collection.find({}, {"pw_hash": 0}).sort("username", 1):
            user["_id"] = str(user["_id"])
            dict_users[str(user["_id"])] = user
        return dict_users
    except:
        return {"error": "Error when retrieving from database"}


def dbremoveUser(_userId):
    try:
        collection = connectDB("sheplaysCadastros")
        if isinstance(collection, Dict) and "error" in collection.keys():
            return collection
        return collection.remove({"_id": ObjectId(_userId)}, justOne=True)
    except:
        return {"error": "error when deleting user"}


# #Receive a document and insert in the database
# def dbinsert(DocumentoInserir):
#     try:
#         collection = connectDB('posts')
#         #Insert the document and print the id
#         doc_id = collection.insert_one(DocumentoInserir).inserted_id
#         print(doc_id)
#     except Exception as e:
#         print (e)
#         print("Error trying to write to database")
#
# def dbretrieve():
#     try:
#         collection = connectDB('posts')
#
#         lista_de_posts = []
#         for post in collection.find().sort("dataPost", -1).limit(10):
#             lista_de_posts.append(post)
#         return lista_de_posts
#     except:
#         print("Error when retrieving from database")
#
# def dbretrievepost(_postId):
#     try:
#         collection = connectDB('posts')
#         post = collection.find_one({"_id": ObjectId(_postId)})
#         return post
#     except:
#         print("error when retrieving the post")
#
# def removepost(_postId):
#     try:
#         collection = connectDB('posts')
#         collection.remove({"_id": ObjectId(_postId)})
#     except:
#         print("error when deleting post")
#
# def updatepost(_postId):
#     try:
#         collection = connectDB('posts')
#         collection.update_one({"_id": ObjectId(_postId)})
#     except:
#         print("error to update post")

# def dbretrievecategoria(_categoria="batata"):
#     try:
#         collection = connectDB('posts')
#         listadeposts = []
#         for post in collection.find({"categoriaPost": {"$regex": _categoria}}):
#             listadeposts.append(post)
#         return listadeposts
#     except:
#         print("error retrieving categorie")


# def dblogaction(loginformation):
#     try:
#         collection = connectDB('logs')
#         collection.insert_one(loginformation)
#     except Exception as e:
#         print(e)
#         print("error when registering log")
#
# def dbretrievenotaprovados():
#     try:
#         collection = connectDB('posts')
#
#         lista_de_posts = []
#         for post in collection.find({"aprovado": False}).sort("dataPost", -1).limit(10):
#             lista_de_posts.append(post)
#         return lista_de_posts
#     except:
#         print("Error when retrieving from database")
