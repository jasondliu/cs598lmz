import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

# Create the client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connect to the "mydatabase" database
mydb = client["mydatabase"]

# Create collection "customers"
mycol = mydb["customers"]

# Insert multiple documents
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name":
