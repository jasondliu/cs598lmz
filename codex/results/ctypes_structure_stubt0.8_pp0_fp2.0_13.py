import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong


class Test:
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x
        self.w = x

    def __repr__(self):
        return '{}'.format(self.x)


class TestS(S):
    def __init__(self, x):
        super().__init__()
        self.x = x
        self.y = x
        self.z = x
        self.w = x

    def __repr__(self):
        return '{}'.format(self.x)


class TestArray:
    def __init__(self, x):
        self.x = x
        self.y = x
        self.z = x
        self.w = x

    def __repr__(self):
        return '{}'.format(self.x)


def test_ndarray():
    a = np.arange(N, dtype=np.float64)
    i = 10
    t
