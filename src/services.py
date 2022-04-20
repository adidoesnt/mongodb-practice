import pymongo
from pymongo.server_api import ServerApi
import certifi

def init():
    ca = certifi.where()
    client = pymongo.MongoClient("mongodb+srv://adi-dev:OeM2j5WzNuRREWK9@test-cluster.c4vlp.mongodb.net/test-database?retryWrites=true&w=majority", server_api=ServerApi('1'), tlsCAFile=ca)
    db = client.test
    print(db.list_collection_names())

init()