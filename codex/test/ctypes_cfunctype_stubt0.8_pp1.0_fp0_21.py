import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hi'

assert isinstance(fun(), str)

class A(ctypes.Structure):
    _fields_ = [("fun", FUNTYPE)]
a = A(fun)
assert isinstance(a.fun(), str)

import pickle
