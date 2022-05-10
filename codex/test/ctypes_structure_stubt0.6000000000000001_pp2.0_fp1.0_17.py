import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    y = ctypes.c_int(2)
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

class W(ctypes.c_void_p):
    def __init__(self, *args, **kwargs):
        super(W, self).__init__(*args, **kwargs)
        self.s = S()

w = W()
w.s.x = 3
