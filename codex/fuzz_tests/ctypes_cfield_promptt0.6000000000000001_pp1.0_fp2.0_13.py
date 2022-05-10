import ctypes
# Test ctypes.CField for structs with non-standard layout
# (i.e. non-standard alignment)
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)
lib.set_alignment.argtypes = ctypes.c_int,

class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                ('b', ctypes.c_int)]

lib.set_alignment(ctypes.alignment(S))
lib.get_alignment.restype = ctypes.c_int
assert lib.get_alignment() == ctypes.alignment(S)

# check the alignment of the fields of 'S'
align = ctypes.alignment(ctypes.c_int)
assert S.a.offset % align == 0
assert S.b.offset % align == 0

# check alignment of the fields of a structure with non-standard alignment
class S2(ctypes.Structure):
    _pack_ = 3
    _fields_ = [('a', ctypes.c_
