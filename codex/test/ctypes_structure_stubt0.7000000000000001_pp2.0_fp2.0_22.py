import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    def __init__(self):
        print("init S")
        self.x = 1

class X(ctypes.Structure):
    _fields_ = [("s", S),
                ("y", ctypes.c_int)]
    def __init__(self):
        print("init X")
        self.y = 2
        super().__init__()

x = X()
print(x.s.x, x.y)
