import ctypes
# Test ctypes.CFUNCTYPE
def myfunc(a, b):
    return a + b

myfunc_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
myfunc_type(myfunc)

# Test ctypes.c_int.from_param
class Foo(object):
    def __init__(self, i):
        self.i = i
    def __int__(self):
        return self.i

c_int = ctypes.c_int.from_param
