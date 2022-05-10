import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    a = ctypes.c_ushort(-1)
    b = a.value % 2
    return b
