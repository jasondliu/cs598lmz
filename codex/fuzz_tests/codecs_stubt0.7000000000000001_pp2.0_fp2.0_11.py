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

class TestUTF32(unittest.TestCase):

    def test_utf32_decoder_error(self):
        # Test UTF-32 decoder errors
        self.assertRaises(UnicodeDecodeError, "abc\xff\xff\xff\xff".decode, "utf-32")
        self.assertRaises(UnicodeDecodeError, "abc\xff\xff\xff".decode, "utf-32")
        self.assertRaises(UnicodeDecodeError, "abc\xff\xff".decode, "utf-32")
        self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-32")
        self.assertRaises(UnicodeDecodeError, "abc".decode, "utf-32")
        self.assertRaises(UnicodeDecodeError, "\xff\xff\xff\xff".decode, "utf-32")
        self.assertRaises(UnicodeDecodeError, "\xff\xff\xff".decode, "utf-32")
        self.
