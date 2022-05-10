import ctypes
# Test ctypes.CField.type
import ctypes._pointer_type_cache
# Test ctypes._SimpleCData_get_value

class X(TestCase):
    def test_cfield_type(self):
        self.assertEqual(ctypes.c_int.type, "i")
        self.assertEqual(ctypes.c_char.type, "c")
        self.assertEqual(ctypes.c_int.type, "i")
        self.assertEqual(ctypes.c_short.type, "h")
        self.assertEqual(ctypes.c_long.type, "l")
        self.assertEqual(ctypes.c_longlong.type, "q")
        self.assertEqual(ctypes.c_ubyte.type, "B")
        self.assertEqual(ctypes.c_ushort.type, "H")
        self.assertEqual(ctypes.c_ulong.type, "L")
        self.assertEqual(ctypes.c_ulonglong.type, "Q")
        self.
