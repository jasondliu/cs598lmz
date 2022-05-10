import _struct
# Test _struct.Struct:
#   struct.Struct is an old-style class (as are all the other struct classes)
#   so that the tests need to use old-style classes as well.

# The following tests are adapted from the unittest for struct.Struct.

# We don't need to test all possible formats, since the format string is
# the same as for the struct module.

class MyStruct(object):
    def __init__(self, fmt):
        self.s = _struct.Struct(fmt)
        self.size = self.s.size

class StructTestCase(unittest.TestCase):

    def test_bool(self):
        # Test packing a bool.
        x = MyStruct('?')
        self.assertEqual(x.s.pack(True), b'\x01')
        self.assertEqual(x.s.pack(False), b'\x00')
        self.assertRaises(TypeError, x.s.pack, 4)

        # Test unpacking a bool.
