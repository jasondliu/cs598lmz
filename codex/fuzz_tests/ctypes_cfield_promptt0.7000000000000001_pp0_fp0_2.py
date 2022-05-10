import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_getitem(self):
        class Test(ctypes.Structure):
            pass
        class Test2(ctypes.Structure):
            _fields_ = [("a", Test), ("b", Test)]
        t = Test2()
        self.assertRaises(TypeError, Test2.__getitem__, t, 2)
        self.assertRaises(TypeError, Test2.__getitem__, Test2, 2)
    def test_setitem(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        class Test2(ctypes.Structure):
            _fields_ = [("a", Test), ("b", Test)]
        t = Test2()
        self.assertRaises(TypeError, Test2.__setitem__, t, 2, 3)
        self.assertRaises(TypeError, Test2.__setitem__, Test2, 2, 3)
    def test_len(self):
       
