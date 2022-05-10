import ctypes
# Test ctypes.CField accordingly
class _CStruct(ctypes._SimpleCData):
    _type_ = "S"
    _subtype_ = "S"
    _length_ = 0
    def __repr__(self):
        return "<_CStruct at %x>" % id(self)

class _CUnion(ctypes._SimpleCData):
    _type_ = "P"
    _subtype_ = "P"
    _length_ = 0
    def __repr__(self):
        return "<_CUnion at %x>" % id(self)

class Test(unittest.TestCase):
    def test_field_from_param(self):
        self.assertEqual(ctypes.CField.from_param(1).value, 1)

    def test_fields(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char * 3),
                        ("c", ctypes.c_short)]
        class Y(ctypes.Union):
           
