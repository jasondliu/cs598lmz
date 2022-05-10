import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    def __init__(self, x, y):
        self.x = x
        self.y = y


# TODO check that python dicts are not allowed to have non-hashable elements
table = ctypes.Structure(
    ("key", (), ctypes.c_int),
    ("value", (), S),
)

data = [
    (0, S(1.0, 2.0)),
    (1, S(3.0, 4.0)),
    (2, S(5.0, 6.0)),
    (3, S(7.0, 8.0)),
    (4, S(9.0, 10.0)),
]

t = table.bind(data)

def test_len():
    assert len(t) == 5

def test_getitem():
    for k, v in data:
        assert t[k] == v

def test_setitem():
    for k, v in data:
        t[k] = v

