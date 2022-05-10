import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"
# This doesn't work.
class C(object):
    def __init__(self):
        self._fun = fun

c = C()
print(c._fun)
