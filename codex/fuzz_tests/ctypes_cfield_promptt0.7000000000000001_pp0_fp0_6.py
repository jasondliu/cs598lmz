import ctypes
# Test ctypes.CField
class Foo(ctypes.Structure):
    pass

Foo._fields_ = [('x', ctypes.c_int)]

print Foo.x


class Bar(ctypes.Structure):
    pass

Bar._fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

print Bar.x
print Bar.y

# Test ctypes.CField
class Foo(ctypes.Structure):
    pass

Foo._fields_ = [('x', ctypes.c_int)]

print Foo.x

# Test ctypes.CFuncPtr
class Foo(ctypes.Structure):
    pass

Foo._fields_ = [('x', ctypes.CFUNCTYPE(ctypes.c_int))]

print Foo.x

class Foo(ctypes.Structure):
    _fields_ = [('x', ctypes.CFUNCTYPE(ctypes.c_int))]

print Foo.x
