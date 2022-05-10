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
