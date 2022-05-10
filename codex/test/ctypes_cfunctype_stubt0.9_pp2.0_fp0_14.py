import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ""

class C:
    def __init__(self):
        self.f = fun
        self.g = self._g
    def _g(self):
        return ""

x = C()
print(dir(x))
