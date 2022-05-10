import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

class C(object):
    @FUNTYPE
    def fun(self):
        return 42

def f():
    x = FUNTYPE(lambda: 42)
    return x()

