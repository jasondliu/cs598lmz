import ctypes
# Test ctypes.CField
import ctypes.test.test_cfield

class MyStructure(ctypes.Structure):
    _fields_ = [("field1", ctypes.c_int),
                ("field2", ctypes.c_int)]

class MyUnion(ctypes.Union):
    _fields_ = [("field1", ctypes.c_int),
                ("field2", ctypes.c_int)]

class MySubStructure(MyStructure):
    _fields_ = [("subfield1", ctypes.c_int)]

class MySubUnion(MyUnion):
    _fields_ = [("subfield1", ctypes.c_int)]

class TestCField(unittest.TestCase):
    def test_structure(self):
        # Test CField.from_address
        obj = MyStructure()
        self.assertRaises(TypeError, ctypes.CField, obj, "field1")
        self.assertRaises(ValueError, ctypes.CField, obj, "field3")
        self.assertEqual(ctypes.
