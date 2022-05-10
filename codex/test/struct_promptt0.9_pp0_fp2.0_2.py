import _struct
# Test _struct.Struct binary string extraction.
import unittest


class TestStruct(unittest.TestCase):
    def test_nullstring(self):
        # Null strings should come out as empty strings.
        # On 64-bit systems, they should have nothing extra at the ends.
        for code in ['s', 'p']:
            for length in [0, 5]:
                fmt = str(length) + code
                structobj = _struct.Struct(fmt)
                s = structobj.pack(b'')
                self.assertEqual(structobj.unpack(s)[0], b'')
                self.assertEqual(structobj.unpack_from(s), (b'',))
                self.assertEqual(structobj.unpack_from(s, 0), (b'',))
                self.assertEqual(structobj.unpack_from(s, 4), (b'',))
                self.assertEqual(list(structobj.iter_unpack(s)), [(b'',)])
