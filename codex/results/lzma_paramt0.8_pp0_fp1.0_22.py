from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# Pickle
import pickle
number = [42, 3.14, 'hello world']
pickled = pickle.dumps(number)
print(pickled)
obj = pickle.loads(pickled)
print(obj)
class Contact:
    def __init__(self, first, last):
        self.first = first
        self.last = last
con = Contact('jason', 'lee')
print(con.first)
pickled = pickle.dumps(con)
print(pickled)

# bz2
import bz2
compressed = bz2.compress(data)
print(len(compressed))
decompressed = bz2.decompress(compressed)
print(len(decompressed))
# zlib
import zlib
compressed = zlib.compress(data)
print(len(compressed))
decompressed = zlib.decompress(compressed)
print(len(decompressed))

# gzip
import gzip
f = open('data
