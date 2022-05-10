import ctypes
# Test ctypes.CField object
library = ctypes.cdll.LoadLibrary("test")

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
print p.x, p.y

fld = POINT._fields_[1]
assert fld.__name__ == 'y'
assert fld.__class__ == ctypes.CField
assert not fld.__dict__
assert fld.offset == ctypes.sizeof(p.x)
assert fld.ctype == ctypes.c_int

try:
    fld.x = 100

except AttributeError:
    pass
else:
    raise AssertionError("no AttributeError")

try:
    del fld.x
except AttributeError:
    pass
else:
    raise AssertionError("no AttributeError")

try:
    p.x = 100
except AttributeError:
    pass
else:
    raise Ass
