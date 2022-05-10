import ctypes
# Test ctypes.CField.from_address()

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

x = X()
x.a = 42
x.b = -42

a = ctypes.c_int.from_address(ctypes.addressof(x))
print(a.value)

a.value = -99
print(x.a)

b = ctypes.c_int.from_address(ctypes.addressof(x), 1)
print(b.value)

b.value = 99
print(x.b)

# Test ctypes.CField.from_buffer()

class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

y = Y()
y.a = 42
y.b = -42

a = ctypes.c_int.from_buffer(y)
print(a.value)


