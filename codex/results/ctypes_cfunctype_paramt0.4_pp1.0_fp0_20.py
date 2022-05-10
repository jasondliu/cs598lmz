import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

f = FUNTYPE(func)
f(2)

#%%
import ctypes
import numpy as np

# Convert the numpy array into a ctypes array.
arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
arr_ctypes = arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

# Pass the ctypes array to the C function.
lib = ctypes.cdll.LoadLibrary('./libtest.so')
lib.test_array(arr_ctypes, len(arr))

# The array has been modified in-place.
print(arr)

#%%
import ctypes
import numpy as np

# Convert the numpy array into a ctypes array.
arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
arr_ctypes = arr.ctypes.
