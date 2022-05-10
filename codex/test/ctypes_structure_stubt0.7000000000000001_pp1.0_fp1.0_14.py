import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()

    def __init__(self, value):
        self.x = value

    def __repr__(self):
        return '<S %d>' % self.x

    def __int__(self):
        return self.x

