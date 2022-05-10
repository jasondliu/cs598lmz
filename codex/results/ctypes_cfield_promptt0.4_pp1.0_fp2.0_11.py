import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_byte),
                        ("b", ctypes.c_short),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_long),
                        ("e", ctypes.c_longlong),
                        ("f", ctypes.c_float),
                        ("g", ctypes.c_double),
                        ("h", ctypes.c_char),
                        ("i", ctypes.c_byte * 4),
                        ("j", ctypes.c_int * 4),
                        ("k", ctypes.c_longlong * 4),
                        ("l", ctypes.c_float * 4),
                        ("m", ctypes.c_double * 4),
                        ("n", ctypes.c_char * 4),
                        ("o", ctypes.c_wchar * 4),
                        ("p", ctypes.c_void_p),
                        ("q", c
