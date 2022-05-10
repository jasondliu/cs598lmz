import _struct
# Test _struct.Struct
# struct.pack
# struct.unpack
# struct.iter_unpack
# struct.unpack_from
# struct.iter_unpack

# Test exception
# struct.error

# Test module
# struct.calcsize
# struct.pack_into
# struct.unpack_from
# struct.iter_unpack
# struct.Struct

class TestStruct(unittest.TestCase):
    def test_class_Struct(self):
        # Test class _struct.Struct
        s = _struct.Struct('i')
        self.assertEqual(s.format, 'i')
        self.assertEqual(s.size, 4)
        self.assertEqual(s.alignment, 4)
        self.assertEqual(s.format_char, 'i')
        self.assertEqual(s.is_native, True)
        self.assertEqual(s.format_code, '@')
        self.assertEqual(s.format_string, '@i')
        self.assertEqual(s.pack_into.__
