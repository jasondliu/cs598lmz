import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField_type(self):
        self.assertEqual(ctypes.CField.__name__, "CField")
        self.assertEqual(ctypes.CField.__module__, "ctypes")

    def test_CField_instance(self):
        self.assertRaises(TypeError, ctypes.CField)

    def test_CField_get_set(self):
        class X(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int),
                ("b", ctypes.c_int),
            ]
        x = X()
        x.a = 1
        x.b = 2
        self.assertEqual(x.a, 1)
        self.assertEqual(x.b, 2)

    def test_CField_set_readonly(self):
        class X(ctypes.Structure):
            _fields_ = [
                ("a", ctypes.c_int),
                ("b", c
