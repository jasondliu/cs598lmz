import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,
                          ctypes.c_int, ctypes.c_int, ctypes.c_void_p)


class Ints:
    def __init__(self, *n):
        self.vals = n
        self.idx = 0

    def next(self):
        idx = self.idx
        self.idx += 1
        return self.vals[idx]


def test_ints_next():
    assert Ints(1, 2, 3).next() == 1
    assert Ints(1, 2, 3).next() == 1
