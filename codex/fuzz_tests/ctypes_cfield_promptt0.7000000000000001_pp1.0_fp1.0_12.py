import ctypes
# Test ctypes.CField


class TestCField(unittest.TestCase):

    def test_simple(self):
        class TestCF(ctypes.Structure):
            _fields_ = [
                ("b", ctypes.c_byte),
                ("c", ctypes.c_char),
                ("h", ctypes.c_short),
                ("i", ctypes.c_int),
                ("l", ctypes.c_long),
                ("q", ctypes.c_longlong),
                ("f", ctypes.c_float),
                ("d", ctypes.c_double),
                ("byte", ctypes.c_ubyte),
                ("char", ctypes.c_ubyte),
                ("short", ctypes.c_ushort),
                ("int", ctypes.c_uint),
                ("long", ctypes.c_ulong),
                ("longlong", ctypes.c_ulonglong),
                ("p", ctypes.c_void_p),
                ("s", ctypes.c_char_p),
                ("w", ctypes.
