import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = ("x", ctypes.c_int), ("fp", ctypes.c_void_p),

class E:
    def __init__(self, fp):
        self.x = "test"
        self.fp = fp

    def __del__(self):
        print("del", self.x)
        self.fp()

