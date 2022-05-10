import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.CField)]
        x = X()
        x.a = 1
        self.assertEqual(x.a, 1)
        self.assertRaises(TypeError, setattr, x, "a", "1")
        try:
            x.a = "1"
        except TypeError as e:
            self.assertEqual(str(e), "must be integer, not str")
        else:
            self.fail("TypeError not raised")
        self.assertRaises(TypeError, setattr, x, "a", 1.5)
        try:
            x.a = 1.5
        except TypeError as e:
            self.assertEqual(str(e), "must be integer, not float")
        else:
            self.fail("TypeError not raised")
        self.assertRaises(TypeError, setattr, x, "a", 1+2
