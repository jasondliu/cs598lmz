import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

class C(object):
    def __init__(self):
        self.f = fun

c = C()
