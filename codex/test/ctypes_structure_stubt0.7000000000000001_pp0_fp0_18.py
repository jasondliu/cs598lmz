import ctypes

class S(ctypes.Structure):
    x = ctypes.c_void_p
    y = ctypes.c_int
    _fields_ = [
        ("y", ctypes.c_int),
        ("x", ctypes.c_void_p),
        ("z", ctypes.c_int),
    ]

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value


class T(ctypes.Structure):
    _fields_ = [
        ("s", S * 5),
    ]


if __name__ == "__main__":
    t = T()
