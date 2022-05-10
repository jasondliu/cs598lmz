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

class TestUnicodeErrorHandling(unittest.TestCase):

    def test_strict(self):
        self.assertRaises(UnicodeDecodeError,
                          "abc\u20ac".encode, "ascii", "strict")
        self.assertRaises(UnicodeEncodeError,
                          "\u20ac".encode, "ascii", "strict")

    def test_replace(self):
        self.assertEqual("abc?\u20ac".encode("ascii", "replace"),
                         b"abc??")
        self.assertEqual(b"abc??".decode("ascii", "replace"),
                         "abc?\ufffd")

    def test_ignore(self):
        self.assertEqual("abc\u20ac".encode("ascii", "ignore"), b"abc")
        self.assertEqual(b"abc".decode("ascii", "ignore"), "abc")

    def test_xmlcharrefreplace(self):
        self.assertEqual
