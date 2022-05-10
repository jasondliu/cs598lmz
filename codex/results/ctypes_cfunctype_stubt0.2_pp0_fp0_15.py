import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class C(object):
    def __init__(self):
        self.fun = fun

c = C()
print c.fun()
</code>

