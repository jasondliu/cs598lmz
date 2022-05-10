import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield_int(self):
        class CFieldTest(ctypes.Structure):
            _fields_ = [("field1", ctypes.c_int)]
        CFieldTest._fields_[0][1]._type_ = "c_int"
        self.assertEqual(CFieldTest._fields_[0][1]._type_, "c_int")

    def test_cfield_int_instance(self):
        class CFieldTest(ctypes.Structure):
            _fields_ = [("field1", ctypes.c_int)]
        CFieldTest._fields_[0][1]._type_ = "c_int"
        self.assertEqual(CFieldTest().field1._type_, "c_int")

    def test_cfield_int_instance_set(self):
        class CFieldTest(ctypes.Structure):
            _fields_ = [("field1", ctypes.c_int)]
        CFieldTest._fields_[0][1
