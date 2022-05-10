import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_none(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.CField)]
        s = S()
        self.assertEqual(s.x, None)

    def test_int(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.CField)]
        s = S()
        s.x = 42
        self.assertEqual(s.x, 42)

    def test_float(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.CField)]
        s = S()
        s.x = 3.14
        self.assertEqual(s.x, 3.14)

    def test_string(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.CField)]
        s = S()
        s.x = "hello"
        self.assert
