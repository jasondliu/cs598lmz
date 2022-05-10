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
assert c_int(1) == 1
assert c_int(Foo(2)) == 2

# Test ctypes.c_int.in_dll
d = ctypes.CDLL(ctypes.util.find_library("c"))
assert ctypes.c_int.in_dll(d, "errno") == 0

# Test ctypes.c_int.from_address
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
x = X()

