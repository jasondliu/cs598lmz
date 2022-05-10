import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

s = S()
print(id(s))
print(s)
s.x = 5
print(s)
print(s.__dict__)

print("-------------------------")

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int), ("z", ctypes.c_int)]

s = S()
print(id(s))
print(s)
s.x = 5
print(s)
print(s.__dict__)



print("-------------------------nstdarray.ctypes_test---- NumpyArray--------------")
import ctypes
import numpy as np
print("------------------- 2D array with 2 column")

two_float_array = np.ndarray(buffer=np.array([1.0, 2.0, 3.0, 4.0], dtype='f4'),
                             dtype='f4',
                             shape=(
