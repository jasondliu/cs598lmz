import ctypes

class S(ctypes.Structure):
    x = ctypes.c_float(1.23)
    y = ctypes.c_float(4.56)

s = S()
assert s.__reduce__()[2] == (1.23, 4.56)


class SWithInit(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()
    def __init__(self):
        self.x = 1.23
        self.y = 4.56

s = SWithInit()
assert s.__reduce__()[2] == (1.23, 4.56)


class SWithInit2(ctypes.Structure):
    x = ctypes.c_float()
    y = ctypes.c_float()
    def __init__(self):
        self.x = 1.23
        self.y = 4.56

s = SWithInit2()
assert s.__reduce__()[2] == (1.23, 4.56)


class SWithInit3(ctypes.Structure):

