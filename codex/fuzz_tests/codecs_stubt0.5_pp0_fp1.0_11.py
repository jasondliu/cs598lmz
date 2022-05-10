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

    def test_decode_error(self):
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b"abc\xff", "strict", True)
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b"abc\xc1", "strict", True)
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b"abc\xff", "strict", False)
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b"abc\xc1", "strict", False)
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode, b"abc\xff", "replace", True)
        self.assertRaises(UnicodeDecodeError,
                          codecs.utf_8_decode,
