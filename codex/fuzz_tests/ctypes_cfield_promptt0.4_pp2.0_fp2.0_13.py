import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

pt = POINT(1, 2)
assert pt.x == 1
assert pt.y == 2

# Test ctypes.CField.from_param
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

    @classmethod
    def from_param(cls, obj):
        if not isinstance(obj, POINT):
            raise TypeError("Wrong type")
        return obj

pt = POINT(1, 2)
assert pt.x == 1
assert pt.y == 2

# Test ctypes.CField.from_param with a list
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

    @classmethod
    def from_param(cls
