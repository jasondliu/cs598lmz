import ctypes
# Test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p)]

class D(C):
    a = ctypes.CField("a")

c = C(b"abc")
assert c.a == b"abc"
assert D.a.__get__(c) == b"abc"
assert D.a.__set__(c, b"def") is None
assert c.a == b"def"

try:
    D.a.__set__(c, "ghi")
except TypeError:
    pass
else:
    raise Exception("expected TypeError")

assert c.a == b"def"

try:
    D.a = "ghi"
except AttributeError:
    pass
else:
    raise Exception("expected AttributeError")

# test ctypes.CField

class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]

class D
