import ctypes
# Test ctypes.CField
class BAR(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class FOO(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("bar", BAR)]

foo = FOO()
foo.a = 1
foo.b = 2
foo.bar.a = 3
foo.bar.b = 4

print(foo.a, foo.b, foo.bar.a, foo.bar.b)

# Test ctypes.CField with a function
def func():
    return 5

class BAZ(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("bar", BAR),
                ("func", ctypes.CFUNCTYPE(ctypes.c_int))]

baz = BAZ()
baz.a = 1
baz.b
