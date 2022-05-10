import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

# Test that CField subclasses PointerType, and that
# we can access the base class
assert issubclass(ctypes.CField, ctypes.POINTER(ctypes.c_int))
assert ctypes.CField._type_

# Test that we can create a CField from a type
f = ctypes.CField(ctypes.c_int)
assert f

# Test that we get the correct type from _type_
assert f._type_ is ctypes.c_int

# Test that we can create a CField from a CField
f = ctypes.CField(f)
assert f

# Test that we get the correct type from _type_
assert f._type_ is ctypes.c_int

# Test that we can create a CField from a POINTER
f = ctypes.CField(ctypes.POINTER(ctypes.c_int))
assert f

# Test that we get the correct type from _type_
assert f._type_ is ctypes.c_int

# Test that we can create a CField from a c
