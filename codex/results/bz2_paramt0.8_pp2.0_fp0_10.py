from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file1_compressed)

#In [5]
from bz2 import BZ2Decompressor

BZ2Decompressor().decompress(file1_compressed) == file1_data

#In [6]

file1_data == file1_data

#In [7]
file1_compressed == file1_compressed

#In [8]
file1_compressed == file1_data

#In [9]

import pickle

file1_pickle = pickle.dumps(file1_data)

#In [10]

import pickle

file1_pickle = pickle.dumps(file1_data)
file2_pickle = pickle.dumps(file2_data)

#In [11]

import pickle

file1_pickle

#In [12]

import pickle

file1_pickle
file2_pickle

#In [13]

import pickle

file1_pickle == file1_
