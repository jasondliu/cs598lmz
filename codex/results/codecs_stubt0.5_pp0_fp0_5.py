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

class TestUTF8(unittest.TestCase):
    def test_bad_utf8_bytes(self):
        # invalid UTF-8 bytes
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "strict")
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "replace")
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "ignore")
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "xmlcharrefreplace")
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "backslashreplace")
        self.assertRaises(UnicodeDecodeError, b"\xff".decode, "utf-8", "
