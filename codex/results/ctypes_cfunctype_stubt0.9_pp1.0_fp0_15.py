import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return np.ones((3,3))

print(type(fun))
print(type(fun()))

# FUNTYPE = ctypes.CFUNCTYPE(np.ctypeslib.ndpointer(dtype=np.float64,ndim=2))
# @FUNTYPE
# def fun():
#     return np.ones((3,3))


# FUNTYPE = ctypes.CFUNCTYPE(
# np.ctypeslib.ndpointer(dtype=np.float64,ndim=2,flags=’C_CONTIGUOUS’))
# @FUNTYPE
# def fun():
#     return np.ones((3,3))

print(type(fun))
print(type(fun()))
</code>


A:

This should work:
<code>import ctypes
from ctypes.util import find_library
from ctypes import cdll, c_void_p, cast, POINTER
from ctypes import CFUNCTYPE
import os

lib = cdll.LoadLibrary(find_library('numpy/core
