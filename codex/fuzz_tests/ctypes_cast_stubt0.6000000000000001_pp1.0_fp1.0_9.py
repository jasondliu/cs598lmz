import ctypes
ctypes.cast(ptr, ctypes.py_object).value

# 8.2.2
# ctypes.POINTER(ctypes.c_int)
#
# ctypes.POINTER(ctypes.c_double)


# 8.2.3
from ctypes import *
import numpy as np

lib = CDLL('./libsample.so')
lib.avg.argtypes = (POINTER(c_int), c_int)
lib.avg.restype = c_double

data = np.random.randint(0, 10, size=5).astype(np.int32)

data_ptr = data.ctypes.data_as(POINTER(c_int))

result = lib.avg(data_ptr, len(data))
print(result)


# 8.2.4
import ctypes
from ctypes import c_int, c_double, c_float
import numpy as np


def pyavg(data):
    n = len(data)
    asum = 0.0
    for i in range(n
