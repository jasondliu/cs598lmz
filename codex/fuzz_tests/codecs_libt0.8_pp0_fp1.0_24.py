import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def connectMongoDB(dbName,collectionName):
    client = MongoClient('mongodb://localhost:27017/')
    db = client[dbName]
    collection = db[collectionName]
    return collection
# collection_qt = connectMongoDB('kol_data','kol_data_qt')

# objlist = collection.find({'_id':{'$gt':'57e2d87c0bd7517b16c5b5a6'}}).limit(100)
# count = 0
# for obj in objlist:
#     count += 1
#     print(obj['_id'])
#     print(obj['nickname'])
#     print(obj['id'])
#     print(obj['followers'])
#     print(obj['city'])
#     print(obj['sex'])
#     print(obj['level'])
#     print(obj['sign'])
#     print(
