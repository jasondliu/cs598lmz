import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(C))]

class D(ctypes.Structure):
    _fields_ = [('n', ctypes.c_int)]

ctypes.CArrayType = type(D._fields_[0][1])

# ctypes.py_object is actually a c_void_p in a lot of implementations
# (including CPython).  It needs to look like a ctypes.py_object.
# Depends on Python implementation details, unfortunately.
ctypes.PyObj_Struct = type(ctypes.py_object)

# CField instance, CArrayType instance and ctypes.py_object are
# treated specially by ctypes_configure.py, so verify that they match
# the expected types.

assert isinstance(S.x, ctypes.CField)
assert isinstance(D._fields_[0][1], ctypes.CArrayType)
assert isinstance(ctypes.py_object, ctypes.PyObj_Struct)
