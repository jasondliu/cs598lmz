import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
            def __init__(self):
                self.a = 1
                self.b = 2
        class Test2(ctypes.Structure):
            _fields_ = [("c", ctypes.c_int),
                        ("d", ctypes.c_int)]
            def __init__(self):
                self.c = 3
                self.d = 4
        class Test3(ctypes.Structure):
            _fields_ = [("e", ctypes.c_int),
                        ("f", ctypes.c_int)]
            def __init__(self):
                self.e = 5
                self.f = 6
        class Test4(ctypes.Structure):
            _fields_ = [("g", ctypes.c_int),
                        ("h", ctypes.c_int)]

