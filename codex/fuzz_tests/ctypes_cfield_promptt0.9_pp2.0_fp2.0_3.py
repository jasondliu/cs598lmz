import ctypes
# Test ctypes.CField
class ctypes_CField_TestBase:
    def test_Simple(self):
        a = self.c_int(42)
        self.assertEqual(a.value, 42)

        class ctypes_CField_TestBase_test_Simple(ctypes.Structure):
            _fields_ = [("integer", self.c_int),
                        ("pointer", ctypes.POINTER(self.c_int))]
        structure = ctypes_CField_TestBase_test_Simple(42)
        structure.pointer = ctypes.pointer(a)
        self.assertEqual(structure.integer, 42)
        self.assertEqual(structure.pointer[0], 42)
        self.assertEqual(ctypes.cast(a, ctypes.c_void_p).value,
                                     ctypes.addressof(structure))
        self.assertEqual(ctypes.cast(structure, ctypes.c_void_p).value,
                                     ctypes.addressof(structure))
        self.assertEqual(ctypes.
