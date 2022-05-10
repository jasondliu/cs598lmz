import ctypes
# Test ctypes.CField

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class RECT(ctypes.Structure):
    def _getx(self): return self.left
    def _setx(self, value): self.left = value
    x = property(_getx, _setx)
    def _gety(self): return self.bottom
    def _sety(self, value): self.bottom = value
    y = property(_gety, _sety)
    _fields_ = [("left", ctypes.c_int),
                ("top", ctypes.c_int),
                ("right", ctypes.c_int),
                ("bottom", ctypes.c_int)]

TheStruct._fields_ = [("an_int", ctypes.c_int),
                      ("a_double", ctypes.c_double),
                      ("a_char", ctypes.c_char),
                      ("a_point", POINT),
                      ("a_rect",
