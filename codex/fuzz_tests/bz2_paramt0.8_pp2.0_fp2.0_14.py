from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

print('inflated {} bytes'.format(len(data)))

# The .bz2 file contains a pickleg object, which is a serialized Python object
# The pickle module is used for serializing and de-serializing objects
# The following command loads the object into the object data
# The module provides 4 methods: dump, dumps, load and loads
# The dumps and loads methods serialize and de-serialize a Python object to and from a string
import pickle

data = pickle.loads(data)

print('found {} enrties:'.format(len(data)))

for date, name, price in data:
    print('판매 날짜: {}, 이름: {}, 가격: {}'.format(date, name, price))
