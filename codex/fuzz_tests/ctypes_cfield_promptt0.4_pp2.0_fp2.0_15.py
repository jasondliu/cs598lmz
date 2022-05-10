import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(Test.a.offset, 0)
        self.assertEqual(Test.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(Test.a.index, 0)

    def test_cfield_array(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int * 3)]

        self.assertEqual(Test.a.offset, 0)
        self.assertEqual(Test.a.size, ctypes.sizeof(ctypes.c_int) * 3)
        self.assertEqual(Test.a.index, 0)

    def test_cfield_nested(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
