import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    z = ctypes.c_double()
    _fields_ = [
        ("x", ctypes.c_double),
        ("z", ctypes.c_double)
    ]

def func(x, y, z):
    print "func", x, y, z
    return 1, 2, 4

def test_py_return_struct():
    m = ctypes.CDLL(os.path.dirname(__file__) + "/modu
