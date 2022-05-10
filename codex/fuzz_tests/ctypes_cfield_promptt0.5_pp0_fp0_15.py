import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class TestClass(ctypes.Structure):
            _fields_ = (ctypes.CField('a'),
                        ctypes.CField('b', ctypes.c_int),
                        ctypes.CField('c', ctypes.c_int, 3))
        self.assertEqual(TestClass.a.offset, 0)
        self.assertEqual(TestClass.a.size, 0)
        self.assertEqual(TestClass.b.offset, 0)
        self.assertEqual(TestClass.b.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(TestClass.c.offset, 0)
        self.assertEqual(TestClass.c.size, 3 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(TestClass), 3 * ctypes.sizeof(ctypes.c_int))
        self.assertRaises(TypeError, c
