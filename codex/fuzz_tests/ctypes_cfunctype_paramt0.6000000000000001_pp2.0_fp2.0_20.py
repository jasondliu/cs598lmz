import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
class A(object):
    def __init__(self, f):
        self.f = FUNTYPE(f)
    def __call__(self, *args):
        return self.f(*args)
</code>

