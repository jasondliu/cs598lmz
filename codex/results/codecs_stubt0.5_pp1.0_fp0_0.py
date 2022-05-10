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

    def test_decode(self):
        # Error handling in the Unicode codecs
        self.assertRaises(UnicodeDecodeError, "\xff".decode, "ascii")
        self.assertRaises(UnicodeDecodeError, "\xff".decode, "ascii", "strict")
        self.assertEqual("\ufffd".decode("ascii", "ignore"), "")
        self.assertEqual("\xff".decode("ascii", "replace"), "\ufffd")
        # "backslashreplace" is an undocumented error handler,
        # but we include it here for completeness
        self.assertEqual("\xff".decode("ascii", "backslashreplace"), "\\xff")
        self.assertEqual("\xff".decode("ascii", "xmlcharrefreplace"), "&#255;")
        self.assertEqual("\u0100".decode("latin-1", "xmlcharrefreplace"),
                         "
