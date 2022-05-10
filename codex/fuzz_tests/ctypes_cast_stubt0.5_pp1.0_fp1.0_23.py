import ctypes
ctypes.cast(id(obj), ctypes.py_object).value

#%%
import numpy as np
from numpy.ctypeslib import ndpointer

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)

print(a)

#%%
import ctypes
import numpy as np

lib = ctypes.CDLL('./lib.so')

lib.add_to_array.argtypes = (ctypes.c_int, ndpointer(ctypes.c_float))
lib.add_to_array.restype = ctypes.c_int

lib.add_to_array(3, a)

print(a)

#%%
import ctypes
import numpy as np

lib = ctypes.CDLL('./lib.so')

lib.add_to_array.argtypes = (ctypes.c_int, ndpointer(ctypes.c_float))
lib.add_to_array.restype = ctypes.c_int

lib.
