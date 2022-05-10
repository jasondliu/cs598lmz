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

class UnicodeDecodeTest(unittest.TestCase):

    def test_decoding_bad_bytes(self):
        # No error handler:
        self.assertRaises(UnicodeDecodeError, b"abc\xff".decode, "ascii")
        self.assertRaises(UnicodeDecodeError, b"abc\xff".decode, "ascii", "strict")
        self.assertRaises(UnicodeDecodeError, b"abc\xff".decode, "ascii", "ignore")
        self.assertRaises(UnicodeDecodeError, b"abc\xff".decode, "ascii", "replace")
        self.assertRaises(UnicodeDecodeError, b"abc\xff".decode, "ascii", "backslashreplace")
        self.assertRaises(UnicodeDecodeError, b"abc\xff".decode, "ascii", "xmlcharrefreplace")

        # Error handler that doesn't add any characters:
        self.assertRaises(Unicode
