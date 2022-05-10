import ctypes
# Test ctypes.CField.
class StructTest(unittest.TestCase):

    def test_CStruct(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]

        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))

    def test_CStruct_incomplete(self):
        class X(ctypes.Structure):
            pass

        self.assertEqual(ctypes.sizeof(X), 0)

    def test_CStruct_POD(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]

            def __init__(self, number):
                self.a = number

        x = X(42)
        self.assertEqual(ctypes.sizeof(x), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(x.a, 42)

    @cpython_only
    def test_CStruct_POD_gc(self
