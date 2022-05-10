import mmap
import sys
import os

# Connect to the database
mongoClient = MongoClient('mongodb://localhost:27017/')
db = mongoClient.test

# Get the database name
databaseName = db.name

# Get the collection name
collectionName = db.comments

# Get the database size
databaseSize = db.command("dbstats")

# Get the documents of the database
documents = collectionName.find()

# Get the number of documents in database
documentsNumber = databaseSize["objects"]

# Get the path to the database
path = databaseSize["dataSize"]


# Get the database name
def database_name():
    print("Database name is: " + databaseName)


# Get the collection name
def collection_name():
    print("Collection name is: " + collectionName.name)


# Get the database size
def database_size():
    print("Database size is: " + str(databaseSize["dataSize"]) + " Bytes")


# Get the number of documents in database
def database_documents_number():
    print("
