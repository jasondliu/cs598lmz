import ctypes
# Test ctypes.CField on is_static_field

class C(ctypes.Structure):
    _fields_ = [("_x", ctypes.c_int),
                ("_y", ctypes.c_int)]

class C(C):
    def getx(self):
        return self._x

lib = ctypes.CDLL(None)
lib.main.restype = ctypes.c_int

expected = 25
result = lib.main()
assert result == expected
