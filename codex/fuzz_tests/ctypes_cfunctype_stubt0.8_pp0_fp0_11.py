import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "42"
</code>
This is a py_object, which is not the same as an object. If you have a function which returns an object, you'll need something like this (using the same example as before, but returning <code>None</code>, which is an object):
<code>from ctypes import *
from ctypes.util import find_library
libc = cdll.LoadLibrary(find_library("c"))
libc.fun.restype = py_object
libc.fun.argtypes = []
print(libc.fun())  # Prints None
</code>

