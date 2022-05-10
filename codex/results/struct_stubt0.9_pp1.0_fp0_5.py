from _struct import Struct
s = Struct.__new__(Struct)
s.rank = 1
s.format = 'i'
binary = conv_binary(s)
binary

s = Struct.__new__(Struct)
s.rank = 1
s.format = 'i'
s.weights = np.array([4])
s.offsets = [0]
s.shape = (1,)
s.itemsize = 4
binary = bytes(conv_binary(s))
binary

with open("data.bin", 'wb') as f:
    f.write(binary)

np.fromfile("data.bin", dtype=np.dtype('i4, f8'))

#%%
import numpy as np
import numpy.core.defchararray as np_strings
import numpy.linalg as la
import sklearn.base as sk_base
import sklearn.utils as sk_utils

class DefaultDict(dict):
    def __getitem__(self, key):
        self.setdefault(key, 0.)
        return dict.__getitem__(self, key)

def categorical_variable
