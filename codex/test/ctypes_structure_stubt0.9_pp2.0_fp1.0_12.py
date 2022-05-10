import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("a", ctypes.c_char_p), ("b", ctypes.c_char_p)]
    def __repr__(self): return "hi"
    def _get_name(self): return "hi"
    name = property(_get_name)

s = S(b"123", b"456")
print(str(s))
