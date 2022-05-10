import ctypes
# Test ctypes.CField

# a simple C structure
class foo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

f = foo()
print f.a, f.b
f.a = 1
f.b = 2
print f.a, f.b

print ctypes.sizeof(f)
print ctypes.addressof(f)

# and now a Structure with a CField
class bar(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.CField("b", ctypes.c_int, 1))]

b = bar()
print b.a, b.b, b.c
b.a = 1
b.b = 2
b.c = 3
print b.a, b.b, b.c

print ctypes.sizeof(b)
print ctypes.addressof(b)

# XXX we need to
