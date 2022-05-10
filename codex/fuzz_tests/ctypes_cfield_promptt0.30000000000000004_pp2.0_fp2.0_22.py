import ctypes
# Test ctypes.CField.from_address
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 1
addr = ctypes.addressof(x)
f = ctypes.CField.from_address(addr, ctypes.c_int)
f.value = 2
print(x.a)

# Test ctypes.CField.from_buffer
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 1
f = ctypes.CField.from_buffer(x, ctypes.c_int)
f.value = 2
print(x.a)

# Test ctypes.CField.from_buffer_copy
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

x = X()
x.a = 1
f = ctypes.CField.from_buffer_copy(x, ctypes.c_int)

