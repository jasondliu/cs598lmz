import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test__init__(self):
        ctypes.CField('a', ctypes.c_int)

    def test_get__set(self):
        class S(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int),
                ("b", ctypes.c_double),
                ("c", ctypes.c_char * 16),
            ]

            def __init__(self):
                self.set_b(2.2)
                self.set_c(b"\x01\x02\x03")
                self.set_a(99)

            def get_a(self):
                return self.a

            def set_a(self, value):
                self.a = value

            def get_b(self):
                return self.b

            def set_b(self, value):
                self.b = value

            def get_c(self):
                return self.c

            def set_c(self, value):
                self
