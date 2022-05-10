import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField("a", 0, 8)),
                ("c", ctypes.CField("a", 8, 8)),
                ("d", ctypes.CField("a", 16, 8))]

x = X()
print(x.a)
x.a = 0x12345678
print(x.a)
print(x.b)
print(x.c)
print(x.d)

x.b = 0x12
print(x.a)
print(x.b)
print(x.c)
print(x.d)

x.c = 0x34
print(x.a)
print(x.b)
print(x.c)
print(x.d)

x.d = 0x56
print(x.a)
print(x.b)
print(x.c)
print(x.d)

# Test ctypes.CField with c_char

