import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2

def get_cfun(name, lib):
    return FUNTYPE(getattr(lib, name))

