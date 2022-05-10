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

class TestCodecs(unittest.TestCase):

    def test_register(self):
        self.assertEqual(codecs.lookup_error("add_one_codepoint"),
                         add_one_codepoint)
        self.assertEqual(codecs.lookup_error("add_utf16_bytes"),
                         add_utf16_bytes)
        self.assertEqual(codecs.lookup_error("add_utf32_bytes"),
                         add_utf32_bytes)

    def test_strict(self):
        self.assertRaises(UnicodeDecodeError,
                          codecs.decode, b"a\x80", "ascii", "strict")
        self.assertRaises(UnicodeDecodeError,
                          codecs.decode, b"a\xc2", "utf-8", "strict")

    def test_ignore(self):
        self.assertEqual(codecs.decode(b"a\x80", "ascii", "ignore"), "
