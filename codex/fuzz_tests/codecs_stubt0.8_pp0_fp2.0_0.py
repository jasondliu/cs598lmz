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
    def test_iso8859_15_decode(self):
        # bug #10517:  ISO-8859-15 does not map U+00A0 to \u00A0
        # http://www.unicode.org/Public/MAPPINGS/ISO8859/8859-15.TXT
        # 0xA0 = \u00A0 = NO-BREAK SPACE
        self.assertEqual("\xa0", "\u00a0".encode("iso-8859-15").decode("iso-8859-15"))

    def test_utf8_decode(self):
        # bug #10983:  UTF-8 decoder fails to detect invalid codepoints
        # XXX: might need to be adjusted when the error handling is changed
        self.assertRaises(UnicodeDecodeError, "\xff".decode, "utf-8", "strict")

    def test_utf_16_32_decode(self):
        # bug #12931:  UTF-16
