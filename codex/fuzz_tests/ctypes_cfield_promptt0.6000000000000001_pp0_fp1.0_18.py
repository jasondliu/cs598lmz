import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

s = S.from_address(ctypes.addressof(S))
for name, type in s._fields_:
    f = getattr(s, name)
    assert type(f) is type

try:
    ctypes.CField("hello", ctypes.c_int)
except TypeError:
    pass
else:
    assert 0, "CField() accepts invalid name"

assert ctypes.CField("_hello", ctypes.c_int).name == "_hello"
