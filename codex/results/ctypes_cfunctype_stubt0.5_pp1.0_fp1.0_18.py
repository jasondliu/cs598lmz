import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class _Test(object):
    def __init__(self):
        self.fun = fun

_Test().fun()
