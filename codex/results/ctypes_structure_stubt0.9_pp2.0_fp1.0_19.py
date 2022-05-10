import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)

with open(__file__, "rb") as f:
    data = f.read()
print(data)

with open(__file__ + ".so", "wb") as f:
    f.write(ctypes.pythonapi.Py_CompileString(data, __file__, __file__))

import __main__

s = S()

import __main__
from ctypes import CDLL

CDLL(__main__.__file__ + ".so").RunModule(__main__.__file__)
----
from ctypes import CFUNCTYPE, cast, c_char_p, c_int, POINTER, c_void_p, py_object, py_object, pythonapi, cast, c_char_p, Py_ssize_t, c_int, c_void_p
from ctypes.util import find_library
from sys import exit

RunModule = pythonapi.Py_RunMain
RunModule.argtypes = [c_char_p]
RunModule.restype = c_int
