import ctypes
# Test ctypes.CField.from_address
import _ctypes_test

lib = ctypes.CDLL(
    os.path.join(os.path.dirname(__file__), "..", "_ctypes_test"))


class X(ctypes.Structure):
    _fields_ = [("b", ctypes.c_byte),
                ("s", ctypes.c_short),
                ("i", ctypes.c_int),
                ("l", ctypes.c_long),
                ("q", ctypes.c_longlong),
                ("p", ctypes.c_void_p),
                ("f", ctypes.c_float),
                ("d", ctypes.c_double)]


class Test(unittest.TestCase):

    def test_long(self):
        addr = lib.ptr_of_x
        x = ctypes.CField.from_address(addr, ctypes.c_long)
        self.assertEqual(x.value, 1234)
        x.value = 7
        self.assertEqual(x.value, 7)

