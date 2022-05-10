import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

C.x = ctypes.c_int

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

C.x = ctypes.c_double

class E(ctypes.Structure):
    _fields_ = [('x', ctypes.CField), ('y', ctypes.c_int)]

print(C.x)
print(D.x)
print(E.x)

# Note:
# The description of CField says:
#
#   If a field is a CField instance, the _length_ field specifies the
#   number of elements.
#
# The _length_ field is not documented, and does not seem to work:

class F(ctypes.Structure):
    _fields_ = [('x', ctypes.CField(5)), ('y', ctypes.c
