import ctypes
# Test ctypes.CField
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_char),
                ("c", ctypes.c_double)]
    C = ctypes.CField(ctypes.c_int, "c")
assert repr(A.C) == "<CField 'C' of 'A' objects>"
assert A.C.offset == ctypes.sizeof(ctypes.c_int) + ctypes.sizeof(ctypes.c_char)
x = A()
assert x.C.offset == A.C.offset
print(x.a, x.b, x.c)
x.a = 1
x.b = b'\x02'
x.c = 3.0
print(x.a, x.b, x.c)
a = ctypes.c_int(4)
ctypes.memmove(ctypes.addressof(x) + x.C.offset, ctypes.addressof(a), ctypes.sizeof(a))
assert x.
