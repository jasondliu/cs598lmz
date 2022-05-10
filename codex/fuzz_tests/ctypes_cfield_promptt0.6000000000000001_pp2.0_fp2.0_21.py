import ctypes
# Test ctypes.CField
assert ctypes.CField is ctypes.Field
# Test ctypes.CField.__doc__
assert ctypes.CField.__doc__ == ctypes.Field.__doc__
# Test ctypes.CField.__get__
field = ctypes.CField(ctypes.c_int, 'field', 0)
assert field.__get__(None, None) is field
assert field.__get__(ctypes.c_int(), None) is field
assert field.__get__(ctypes.c_int(), ctypes.c_int) is field
class X(ctypes.Structure):
    _fields_ = [('field', ctypes.c_int)]
assert X.field.__get__(None, None) is X.field
assert X.field.__get__(X(), None) is X.field
assert X.field.__get__(X(), X) is X.field
assert X.field.__get__(X(), X()) is X().field
# Test ctypes.CField.__set__
X.field.__set__(None,
