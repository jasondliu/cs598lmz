from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'Hello World!'))

import zlib
s = zlib.compress(b'Hello World!')
zlib.decompress(s)

# Compress Objects
import bz2
original_data = [b'This is the content', b'of the original file', b'.']
f = bz2.open('bziptest.bz2', 'wt')
f.writelines(original_data)
f.close()

import bz2
f = bz2.open('bziptest.bz2', 'rt')
f.readlines()

# Storage and Retrieval of Python Objects
p = pickle.dumps(object)
object = pickle.loads(p)

import pickle
f = open(r'pickletest.pkl', 'wb')
pickle.dump(original_data, f)
f.close()

import pickle
f = open(r'pickletest.pkl', 'rb')
data = pickle.load(f)

