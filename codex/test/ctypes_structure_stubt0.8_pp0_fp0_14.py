import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

    def __init__(self, foo):
        self.x = foo

    def __repr__(self):
        x = self.x
        return ctypes.string_at(ctypes.addressof(x), ctypes.sizeof(x))[::-1].encode('hex')


s = S(2)
