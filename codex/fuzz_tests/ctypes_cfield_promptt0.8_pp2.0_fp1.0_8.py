import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_ushort)]
        self.assertEqual(ctypes.sizeof(X), 2)

        class Y(X):
            _fields_ = [("b", ctypes.c_ushort)]
        self.assertEqual(ctypes.sizeof(Y), 4)

        self.assertEqual(ctypes.sizeof(ctypes.c_ushort), 2)

        class Z(Y):
            _fields_ = [("c", ctypes.c_ubyte)]
        self.assertEqual(ctypes.sizeof(Z), 5)

        class W(Y):
            _fields_ = [("c", ctypes.c_ulong)]
        self.assertEqual(ctypes.sizeof(W), 8)

        class A(ctypes.Structure):
            _fields_ = [("a", ctypes.c_ubyte),
                       
