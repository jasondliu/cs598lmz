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

class CodecsModuleTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(codecs.escape_encode(b"abc"), (b"abc", 3))
        self.assertEqual(codecs.escape_decode(b"abc"), ("abc", 3))

        self.assertEqual(codecs.escape_decode(b"\\N{GREEK SMALL LETTER SIGMA}"),
                         ("\u03c3", 28))
        self.assertEqual(codecs.escape_encode("\u03c3"), (b"\\u03c3", 6))

        self.assertEqual(codecs.escape_encode("\u03c3", "backslashreplace"), (b"\\\\u03c3", 8))
        self.assertEqual(codecs.escape_decode(b"\\\\"), ("\\", 2))

        self.assertRaises(UnicodeEncodeError, codecs.escape_encode, "\\")

    def test_as
