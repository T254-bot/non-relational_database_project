import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myFirstDB"
COLLECTION = "celebrities"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailiure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]
"""
- Inserts one new document into database:
new_doc = {"first": "douglas", "last": "adams", "dob": "11/03/1952", "hair_colour": "grey", "occupation": "writer", "nationality": "british"}

coll.insert_one(new_doc)
"""
"""
- Inserts mulitple documents into database:
new_docs = [{
    "first": "terry",
    "last": "pratchet",
    "dob": "28/04/1948",
    "hair_colour": "not much",
    "occupation": "writer",
    "nationality": "british"
}, {    
    "first": "george",
    "last": "rr martin",
    "dob": "20/09/1948",
    "hair_colour": "white",
    "occupation": "writer",
    "nationality": "american"
}]

coll.insert_many(new_docs)
"""
"""
- Finds specific document:
documents = coll.find({"first": "douglas"})

- Finds all documents
documents = coll.find()
"""
#NOT WORKING
#coll.remove({"first": "douglas"})

coll.update_many({"nationality": "american"}, {"$set": {"hair_colour": "maroon"}})

documents = coll.find({"nationality": "american"})

for doc in documents:
    print(doc)