import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

assert int(fun()) == 1

TYPE = ctypes.CFUNCTYPE(ctypes.c_int)
@TYPE
def fun():
    return 1

assert fun() == 1

TYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
@TYPE
def sum(a, b):
    return a + b

assert sum(1, 2) == 1 + 2

assert sum(-1, 2) == -1 + 2

assert sum(-1, -2) == -1 - 2

assert sum(-2, -2) == -2 - 2

def get_ctypes_dso():
    import ctypes
    import os
    path = os.path.join(os.path.dirname(__file__), 'ctypes_dso')
    ctypes_dso = ctypes.CDLL(path)
    return ctypes_dso

try:
    ctypes_dso = get_ctypes_dso()
except OSEr
