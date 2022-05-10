import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        # Test that ctypes.CField works as expected
        # See issue #18

        class MyStruct(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int)]

        self.assertEqual(MyStruct.a.offset, 0)
        self.assertEqual(MyStruct.b.offset, ctypes.sizeof(ctypes.c_int))

        class MyStruct2(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int),
                        ('c', ctypes.c_int)]

        self.assertEqual(MyStruct2.a.offset, 0)
        self.assertEqual(MyStruct2.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(MyStruct2.c.offset, 2 * ctypes.sizeof(ctypes
