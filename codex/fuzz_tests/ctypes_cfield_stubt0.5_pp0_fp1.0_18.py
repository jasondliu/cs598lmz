import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

#
# The following tests are for the CField_get and CField_set methods.
#

#
# First test for the __get__ method
#
s = S()
s.x = 42
assert s.x == 42

assert S.x.__get__(s, None) == 42
assert S.x.__get__(s, S) == 42

try:
    S.x.__get__(None, None)
except TypeError:
    pass
else:
    print('expected TypeError')

try:
    S.x.__get__(None, S)
except TypeError:
    pass
else:
    print('expected TypeError')

try:
    S.x.__get__(s, C)
except TypeError:
    pass
else:
    print('expected TypeError')

#
# Now test for the __set__ method
#
s = S()
assert s.x ==
