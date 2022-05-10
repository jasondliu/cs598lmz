import ctypes
# Test ctypes.CField
class CFieldTestCase(BaseTestCase):
    def test_type(self):
        class C(ctypes.Structure):
            _fields_ = [
                ('x', ctypes.c_int),
                ('y', ctypes.c_short),
                ('z', ctypes.c_long)
            ]
        self.assertEqual(ctypes.sizeof(C), ctypes.c_int.size + ctypes.c_short.size + ctypes.c_long.size)
        self.assertEqual(C.x.offset, 0)
        self.assertEqual(C.y.offset, ctypes.c_int.size)
        self.assertEqual(C.z.offset, ctypes.c_int.size + ctypes.c_short.size)
        self.assertEqual(C.x.size, ctypes.c_int.size)
        self.assertEqual(C.y.size, ctypes.c_short.size)
        self.assertEqual(C.z.size, ctypes.c_
