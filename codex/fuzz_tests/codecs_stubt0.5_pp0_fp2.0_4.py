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

class TestUnicodeDecode(unittest.TestCase):
    def test_wrong_type(self):
        self.assertRaises(TypeError, codecs.utf_16_decode, 42)

    def test_wrong_size(self):
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff\xfe\x00')
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff\xfe\x00\x00\x00')

    def test_empty_string(self):
        self.assertEqual(codecs.utf_16_decode(b''), ("", 0))
        self.assertEqual(codecs.utf_16_decode(b'', 'strict'), ("", 0))
        self.assertEqual(codecs.utf_16_decode(b'', 'ignore'), ("", 0))
        self.assertEqual(codecs.utf_16_decode(
