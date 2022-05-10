import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Union):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CUnion = type(X.y)

#
# Create a few instances.
#

s = S()
s.x = 42
s2 = S(42)
s3 = S(x=42)
s4 = S()
s4.x = 42
assert s == s2 == s3 == s4

u = X()
u.y = 42
u2 = X(42)
u3 = X(y=42)
u4 = X()
u4.y = 42
assert u == u2 == u3 == u4

#
# Classes can be used as metaclasses
#

class mymeta(type):
    def __new__(cls, name, bases, dct):
        print("creating class", name)
        if not name.startswith("my"):
            raise TypeError("class name must start with 'my'")
        return type.__new__(cls, name,
