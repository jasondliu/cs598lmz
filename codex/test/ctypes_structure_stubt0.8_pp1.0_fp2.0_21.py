import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longdouble()
    y = ctypes.c_longdouble()

class fake_zlib:
    def __init__(self):
        self.crc32 = 0

