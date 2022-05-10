import lzma
lzma.__file__

# Download data from https://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip
# put in /data

def parse(path):
  g = open(path, 'r')
  for l in g:
    yield eval(l)

MONGO_DB = {
    'host': '0.0.0.0',
    'port': 27017,
    'db_name': 'yelp'
}

# Get collection
client = MongoClient(host=MONGO_DB['host'], port=MONGO_DB['port'])
db = client[MONGO_DB['db_name']]

# insert data
i = 0

for d in parse('../data/reviews_Home_and_Garden_5.json'):
    i += 1
    db.reviews_Home_and_Garden_5.insert_one(d)
    if i % 1 == 0:
        print('Processed {} records, last review id: {}'.format(i, d['review_id
