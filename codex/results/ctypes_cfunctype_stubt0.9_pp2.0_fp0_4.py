import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class R(object):

    def f(self, arg):
        return arg + 1

r = R()
r.f = f
