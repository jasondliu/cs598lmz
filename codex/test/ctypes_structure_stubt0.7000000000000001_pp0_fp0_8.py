import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint8
    y = ctypes.c_uint8
    _pack_ = 1

class C(object):
    def __init__(self):
        self._s = S()

    def set(self, x, y):
        self._s.x = x
        self._s.y = y

    def get(self):
        return self._s.x, self._s.y

if __name__ == '__main__':
    c = C()
    c.set(0x11, 0x22)
