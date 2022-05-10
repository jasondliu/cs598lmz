import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

# Create the client
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Connect to the "mydatabase" database
mydb = client["mydatabase"]

# Create collection "customers"
mycol = mydb["customers"]

# Insert multiple documents
