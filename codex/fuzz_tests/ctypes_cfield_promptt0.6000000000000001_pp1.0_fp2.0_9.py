import ctypes
# Test ctypes.CField.
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class c_struct(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int),
                        ('y', ctypes.c_int)]
        self.assertEqual(ctypes.c_int.in_dll(c_struct, "x").value, 0)
        self.assertEqual(ctypes.c_int.in_dll(c_struct, "y").value, 0)
        c_struct.x = 42
        self.assertEqual(ctypes.c_int.in_dll(c_struct, "x").value, 42)
        self.assertEqual(ctypes.c_int.in_dll(c_struct, "y").value, 0)
        c_struct.y = 43
        self.assertEqual(ctypes.c_int.in_dll(c_struct, "x").value, 42)
        self.assertEqual(ctypes.c_int.in_dll(c_
