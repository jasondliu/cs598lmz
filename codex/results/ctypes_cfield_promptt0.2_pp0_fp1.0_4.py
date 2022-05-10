import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class CFIELD(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int),
                        ("e", ctypes.c_int),
                        ("f", ctypes.c_int),
                        ("g", ctypes.c_int),
                        ("h", ctypes.c_int),
                        ("i", ctypes.c_int),
                        ("j", ctypes.c_int),
                        ("k", ctypes.c_int),
                        ("l", ctypes.c_
