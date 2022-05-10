import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(12)

class Test(object):
    def __init__(self, a):
        self.value = a

    def __int__(self):
        return self.value

    def __index__(self):
        return self.value

s = S()

