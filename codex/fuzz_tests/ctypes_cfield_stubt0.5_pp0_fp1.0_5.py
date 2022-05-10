import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('f', ctypes.CField)]

c = C()
c.f = 1
print c.f
print c.f.__class__

# The following is a bit tricky, but the idea is to test
# that the _fields_ attribute of the returned object is
# the same as the _fields_ attribute of the CField type.
# This is important because the _fields_ attribute is
# used for the __getattr__ and __setattr__ methods of
# Structure and Union.

print C._fields_[0][1]._fields_ is ctypes.CField._fields_

# test that ctypes.CField is a subclass of ctypes._Pointer

print issubclass(ctypes.CField, ctypes._Pointer)

# test that ctypes.CField instances are instances of ctypes._Pointer

print isinstance(c.f, ctypes._Pointer)

# test that ctypes.CField instances have the same _type_ attribute
# as the _type_ attribute
