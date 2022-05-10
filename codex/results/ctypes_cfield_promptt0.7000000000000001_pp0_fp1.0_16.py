import ctypes
# Test ctypes.CField.__repr__
assert repr(ctypes.c_int.value) == "<CField 'value' of 'c_int' objects>"
class X(ctypes.Structure):
    _fields_ = [("field", ctypes.c_int)]
# Test ctypes.CField.__repr__
assert repr(ctypes.c_int.value) == "<CField 'value' of 'c_int' objects>"
assert repr(X.field) == "<CField 'field' of 'X' objects>"
assert str(X.field) == "c_int(0)"
# Casting from a class instance to a pointer to the class
# should work
assert ctypes.cast(X(), ctypes.POINTER(X))
# Test ctypes.CPointer.__repr__
assert repr(ctypes.c_void_p) == "<class 'ctypes.c_void_p'>"
b = ctypes.c_byte(3)
assert repr(ctypes.pointer(b)) == "<ctypes.LP_c_byte object at 0x%x>" % (id
