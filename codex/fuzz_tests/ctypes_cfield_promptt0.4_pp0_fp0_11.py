import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_char)]
    _anonymous_ = ("b",)

s = S()
print s.a, s.c
s.a = "A"
s.c = "C"
print s.a, s.c
try:
    s.b
except AttributeError:
    print "AttributeError: b"

# Test ctypes.CField.from_address()
class S2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.c_char)]
    _anonymous_ = ("b",)

s2 = S2()
s2.a = "A"
s2.c = "C"

s3 = S2.from_address(ctypes.addressof(s2))
print s3.a
