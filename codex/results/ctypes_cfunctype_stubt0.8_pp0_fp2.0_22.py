import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("Hello")
    return "World"

print(fun())

# (b)
from ctypes import *
from ctypes import util
lib = cdll.LoadLibrary(util.find_library("libpng")) # e.g.
lib.png_write_end.argtypes = [c_void_p, c_void_p]
lib.png_write_end.restype = None
</code>

