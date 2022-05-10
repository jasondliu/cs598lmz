import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

import numpy as np
import ctypes

def get_id(x):
    return ctypes.cast(id(x), ctypes.py_object).value

a = np.zeros((10,10))
b = np.zeros((10,10))

print(get_id(a) == get_id(b))

#%%

import numpy as np
import ctypes

def get_id(x):
    return ctypes.cast(id(x), ctypes.py_object).value

a = np.zeros((10,10))
b = np.zeros((10,10))

print(get_id(a) == get_id(b))

#%%

import numpy as np
import ctypes

def get_id(x):
    return ctypes.cast(id(x), ctypes.py_object).value

a = np.zeros((10,10))
b = np.zeros((10,10))


