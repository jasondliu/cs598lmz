import bz2
# Test BZ2Decompressor

key_file = './data/key.bz2'
f = bz2.BZ2File(key_file)
res = f.read()
print(res)

# Test BZ2Compressor

f = bz2.BZ2File(key_file, 'w')
f.write(res + b'\n')

f.close()
import zlib
# Test zlib

key_file = './data/key.zlib'
f = zlib.compress(res)
print(f)
res_unz = zlib.decompress(f)
print(res_unz)

import os
os.remove(key_file)

import pickle
# Test pickle

key_file = './data/key.pickle'

#dump
f = open(key_file, 'wb')
pickle.dump(res, f)
f.close()

#load
f = open(key_file, 'rb')
res_unpickle = pickle.load(f)

print
