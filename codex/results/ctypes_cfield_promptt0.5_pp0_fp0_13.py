import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField_c_type(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.CField)]
        self.assertEqual(C._fields_[0][1], ctypes.CField)
        self.assertEqual(C.a.__class__, ctypes.CField)
        self.assertEqual(C.a.__name__, "a")
        self.assertEqual(C.a.offset, 0)
        self.assertEqual(C.a.size, ctypes.sizeof(ctypes._CFuncPtr))
        self.assertEqual(C.a.index, 0)
        self.assertEqual(C.a.pack, 1)
        self.assertEqual(C.a.c_type, ctypes._CFuncPtr)

    def test_CField_from_address(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.C
