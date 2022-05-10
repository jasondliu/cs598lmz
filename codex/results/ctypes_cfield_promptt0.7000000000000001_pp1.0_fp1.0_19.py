import ctypes
# Test ctypes.CField instance creation

class Test(ctypes.Structure):
    _fields_ = [("foo", ctypes.c_int)]

try:
    Test._fields_.append(("bar", Test.foo))
except TypeError:
    raise Exception("CField instance creation failed")

# Test ctypes.CField instance re-use

try:
    Test._fields_.append(("baz", Test.bar))
except TypeError:
    raise Exception("CField instance re-use failed")

# Test ctypes.CField instance re-use with a new type

try:
    Test._fields_.append(("baz", Test.bar))
except TypeError:
    raise Exception("CField instance re-use with a new type failed")
