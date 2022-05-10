import _struct
# Test _struct.Struct
import _testcapi

# XXX We could import all the type names, but what if one is shadowed in the
# local scope?
#for k, v in _testcapi._STRUCT_FIELDS.items():
#    globals()[k] = v
Py_ssize_t = _testcapi.Py_ssize_t
Py_UNICODE = _testcapi.Py_UNICODE
Py_UCS4 = _testcapi.Py_UCS4

# The following structures don't work yet.
# struct_with_mixed_pointers
# struct_with_object_as_first_member
# struct_with_object_in_the_middle
# struct_with_object_as_last_member
# struct_with_two_objects

class StructTest(unittest.TestCase):
    def test_basics(self):
        simple_struct = "i"
        s = _struct.Struct(simple_struct)
        self.assertEqual(s.size, _struct.calcsize(simple_struct))
        self
