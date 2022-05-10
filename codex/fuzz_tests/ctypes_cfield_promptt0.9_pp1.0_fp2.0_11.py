import ctypes
# Test ctypes.CField and ctypes.c_void_p
# in the context of a structure.
import _ctypes_test

try:
    ctypes.CField
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

lib = ctypes.CDLL(_ctypes_test.__file__)

class POINT(ctypes.Structure):
    pass

POINT._fields_ = [
    ('x', ctypes.c_int),
    ('y', ctypes.c_int),
]

Element = POINT._fields_[0][0]
assert 'name' in Element.__dict__
assert 'offset' in Element.__dict__
assert not '_length_' in Element.__dict__

lib.get_point.restype = POINT
lib.get_point.argtypes = []

class POINTER(ctypes.Structure):
    pass

POINTER._fields_ = [
    ('p', ctypes.c_void_p)
]

lib.get_pointer.restype = POINTER

