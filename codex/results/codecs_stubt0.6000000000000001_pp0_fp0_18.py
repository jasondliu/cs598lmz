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

class TestUtf8(unittest.TestCase):
    def test_utf8_decode_error(self):
        for i in range(0, 0x100):
            self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-8", "strict")
            self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-8", "replace")
            self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-8", "ignore")
            self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-8", "add_one_codepoint")
            self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-8", "add_utf16_bytes")
            self.assertRaises(UnicodeDecodeError, "abc\xff".decode, "utf-8", "add_utf32_bytes")

        self.assertEqual("abc
