import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [('value', ctypes.CField)]

assert ctypes.sizeof(X) == ctypes.sizeof(ctypes.c_void_p)

x = X()
x.value = 42
assert x.value == 42

# Test alignment

class X(ctypes.Structure):
    _fields_ = [('value', ctypes.CField * 2)]

assert ctypes.sizeof(X) == ctypes.sizeof(ctypes.c_void_p) * 2

x = X()
x.value[0] = 42
x.value[1] = 24
assert x.value[0] == 42
assert x.value[1] == 24

class X(ctypes.Structure):
    _fields_ = [('value', ctypes.CField * 3)]

assert ctypes.sizeof(X) == ctypes.sizeof(ctypes.c_void_p) * 3

x = X()
x.value[0] = 42
x.
