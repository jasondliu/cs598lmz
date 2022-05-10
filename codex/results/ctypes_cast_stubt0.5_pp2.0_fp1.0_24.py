import ctypes
ctypes.cast(None, ctypes.py_object)

import numpy as np 
import numpy.ctypeslib as npct 
array_1d_double = npct.ndpointer(dtype=np.double, ndim=1, flags='CONTIGUOUS') 

libcd = npct.load_library("libcdemo", ".") 
libcd.cdemo.restype = None 
libcd.cdemo.argtypes = [array_1d_double, array_1d_double, ctypes.c_int] 

a = np.array([1., 2., 3., 4., 5.], dtype=np.double) 
b = np.array([1., 2., 3., 4., 5.], dtype=np.double) 

print(a, b) 
libcd.cdemo(a, b, len(a)) 
print(a, b)

#  g++ -c -fPIC cdemo.cpp -o cdemo.o
#  g++ -shared -Wl,-soname,lib
