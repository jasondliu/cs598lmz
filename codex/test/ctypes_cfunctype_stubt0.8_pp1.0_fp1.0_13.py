import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    # return ctypes.c_void_p(None)
    return None

class W:
    def __init__(self, t=None, f=None):
        self.t = t
        self.f = f
    def some(self):
        return self.t
    def none(self):
        return self.f

w = W(t='v', f=None)
print(w)
x = w.some()
y = w.none()
print(x)
print(y)
