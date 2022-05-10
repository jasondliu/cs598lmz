import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield_init(self):
        # Test a simple CField
        class CFieldTest(ctypes.Structure):
            _fields_ = [("field1", ctypes.c_int)]
        self.assertEqual(CFieldTest.field1.offset, 0)
        self.assertEqual(CFieldTest.field1.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(CFieldTest.field1.index, 0)
        self.assertEqual(CFieldTest.field1.bitshift, 0)
        # Test a CField with a bitfield
        class CFieldBitFieldTest(ctypes.Structure):
            _fields_ = [("field1", ctypes.c_int, 2)]
        self.assertEqual(CFieldBitFieldTest.field1.offset, 0)
        self.assertEqual(CFieldBitFieldTest.field1.size, ctypes.sizeof(ctypes.c_int))
        self.assert
