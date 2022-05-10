import ctypes
# Test ctypes.CField
assert ctypes.CField(None, None, None, None, None, None, None) is None

# Test ctypes.CField.from_address
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

x = X()
assert ctypes.CField.from_address(ctypes.addressof(x), ctypes.c_int) == x.a

# Test ctypes.CField.from_param
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

x = X()
assert ctypes.CField.from_param(x.a) == x.a

# Test ctypes.CField.in_dll
class X(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

x = X()
lib = ctypes.CDLL(None)
lib.x = x
assert ctypes.CField.in_dll(lib, 'x') == x

# Test ctypes
