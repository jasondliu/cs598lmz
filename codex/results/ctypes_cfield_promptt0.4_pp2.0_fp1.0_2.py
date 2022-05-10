import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        # Test ctypes.CField
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 16),
                        ("c", ctypes.c_int, 16),
                        ("d", ctypes.c_int, 8),
                        ("e", ctypes.c_int, 8),
                        ("f", ctypes.c_int, 4),
                        ("g", ctypes.c_int, 4),
                        ("h", ctypes.c_int, 2),
                        ("i", ctypes.c_int, 2),
                        ("j", ctypes.c_int, 1),
                        ("k", ctypes.c_int, 1),
                        ("l", ctypes.c_int, 1),
                        ("m", ctypes.c_int, 1),
                        ("n", ctypes.c_int, 1),
                        ("o", ctypes.c_int, 1
