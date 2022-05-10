import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField_instance(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertIsInstance(Test.a, ctypes.CField)
        self.assertIsInstance(Test().a, ctypes.CField)

    def test_CField_name(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(Test.a.name, "a")
        self.assertEqual(Test().a.name, "a")

    def test_CField_offset(self):
        class Test(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(Test.a.offset, 0)
        self.assertEqual(Test().a.offset, 0)

    def test_CField_type(self):
        class Test(ctypes.St
