import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())

from ctypes import cdll
lib = cdll.LoadLibrary(None)
print(lib.time(None))

import ctypes
from datetime import date
today = date.today()
print(today)
