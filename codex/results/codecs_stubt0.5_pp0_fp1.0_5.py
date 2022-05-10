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

    def test_register_error(self):
        self.assertEqual(codecs.lookup_error("add_one_codepoint"), add_one_codepoint)
        self.assertEqual(codecs.lookup_error("add_utf16_bytes"), add_utf16_bytes)
        self.assertEqual(codecs.lookup_error("add_utf32_bytes"), add_utf32_bytes)

    def test_lookup_error(self):
        self.assertRaises(LookupError, codecs.lookup_error, "unknown_handler")

    def test_strict_errors(self):
        self.assertRaises(UnicodeDecodeError, codecs.decode, b"abc\xff", "ascii", "strict")
        self.assertRaises(UnicodeEncodeError, codecs.encode, "abc\u20ac", "ascii", "strict")

    def test_ignore_errors(self):

