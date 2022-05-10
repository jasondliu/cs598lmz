import ctypes
# Test ctypes.CField
ctypes.CField('foo', None)
ctypes.CField('foo', ctypes.c_int)
try:
    ctypes.CField('', ctypes.c_int)
except ValueError:
    pass
else:
    raise Exception
try:
    ctypes.CField(None, None)
except RuntimeError:
    pass
else:
    raise Exception

# Test ctypes.Field
class X(ctypes.Structure):
    _fields_ = [('f2', ctypes.c_int), ('f1', ctypes.c_char)]
assert ctypes.Field(X, "f1", ctypes.c_char)
try:
    ctypes.Field(X, "f1", ctypes.c_int)
except TypeError:
    pass
else:
    raise Exception
try:
    ctypes.Field(X, "f99", ctypes.c_int)
except ValueError:
    pass
else:
    raise Exception
try:
    ctypes.Field(X, "f1", None)
except TypeError
