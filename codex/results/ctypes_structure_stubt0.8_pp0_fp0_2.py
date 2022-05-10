import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [("x", ctypes.c_int)]
    def __getattr__(self, name):
        if name == "x":
            return 'x'
print(S().x)
