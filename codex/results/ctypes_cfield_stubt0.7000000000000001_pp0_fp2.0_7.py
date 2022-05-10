import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)

del S.x
try:
    S.x   # should be gone
except AttributeError:
    pass
else:
    raise Exception("should be gone")

#

try:
    ctypes.CField()
except TypeError:
    pass
else:
    raise Exception("should not allow construction")

#

ctypes.CField.__doc__ = "should not throw"

#

S._fields_ = [('x', ctypes.c_int)]
try:
    S.x = "spam"
except TypeError:
    pass
else:
    raise Exception("should not allow assignment")

#

try:
    del S.x
except AttributeError:
    pass
else:
    raise Exception("should not allow deletion")
