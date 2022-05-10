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

class TestDecoding(unittest.TestCase):
    def test_ascii(self):
        self.assertEqual(codecs.decode(b"abc", "ascii"), "abc")
        self.assertEqual(codecs.decode(b"abc\xff", "ascii", "replace"), "abc?")
        self.assertEqual(codecs.decode(b"abc\xff", "ascii", "ignore"), "abc")
        self.assertEqual(codecs.decode(b"abc\xff", "ascii", "xmlcharrefreplace"), "abc&#255;")
        self.assertRaises(UnicodeDecodeError, codecs.decode, b"abc\xff",
                          "ascii", "strict")
        self.assertEqual(codecs.decode(b"abc\xff", "ascii", "add_one_codepoint"), "abca")
        self.assertRaises(UnicodeDecodeError, codecs.decode,
