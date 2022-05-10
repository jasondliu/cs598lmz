import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint16(65535)
    y = ctypes.c_int64(0)
    z = ctypes.c_uint8(255)

    def __init__(self):
        super(S, self).__init__()
        self.y = 0
        self.z = 255

a = S()

