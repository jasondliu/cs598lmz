import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class TestDecode(unittest.TestCase):

    def test_latin1(self):
        # Test decoding Latin-1
        self.assertEqual(
            codecs.latin_1_decode(b'abcdefghijklmnopqrstuvwxyz\xe0\xe7\xec\xf2\xf9'),
            ('abcdefghijklmnopqrstuvwxyz\xe0\xe7\xec\xf2\xf9', 26))
        self.assertEqual(
            codecs.latin_1_decode(b'\xff'),
            ('\ufffd', 1))
        self.assertEqual(
            codecs.latin_1_decode(b'\xff', 'strict'),
            ('\ufffd', 1))
        self.assertRaises(UnicodeDecodeError,
            codecs.latin_1_decode, b'\xff', 'ignore')
        self.assertRaises(UnicodeDecodeError,
            codecs.latin_1
