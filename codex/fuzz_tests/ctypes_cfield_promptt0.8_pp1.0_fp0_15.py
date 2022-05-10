import ctypes
# Test ctypes.CField instance
#@@CTYPES_DOES_NOT_SUPPORT_FIELD_NAMES@@
class POINT(ctypes.Structure):
    _fields_ = (("x", ctypes.c_int),
                ("y", ctypes.c_int))
    _field_ = ("x", ctypes.c_int) # TypeError: field is not a string

class RECT(ctypes.Structure):
    _fields_ = (("a", POINT),
                ("b", POINT))
    _field_ = (("a", POINT), ("b", POINT)) # TypeError: field is not a string
#@@CTYPES_DOES_NOT_SUPPORT_FIELD_NAMES@@

# Check that FIELD_TYPE is ctypes.Structure subclass
class S(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class SChild(S):
    _fields_ = [("b", ctypes.c_int)]

# A typedef to a type defined at the C level
libc = ctypes.
