import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print("CField type", type(S.x))
print("CField instance", S.x)

try:
    ctypes.Field = S.x
except TypeError:
    exc = sys.exc_info()[1]
    print(exc)
else:
    print("should have raised TypeError")

################################################################
#
# Verify that a CField instance is usable as a non-recursive base.
#

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

class T(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('_b', S),
                ('c', ctypes.c_int)]
    _anonymous_ = ['_b']

S.x = ctypes.c_int
S.z = ctypes.c_int
T._b = S
T.b = property(lambda self: self._b, doc="b_doc")

s = S
