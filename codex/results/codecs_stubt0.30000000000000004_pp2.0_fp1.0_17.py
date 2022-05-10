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

    def test_decode(self):
        self.assertEqual(codecs.decode("abc", "ascii"), b"abc")
        self.assertEqual(codecs.decode(b"abc", "ascii"), "abc")
        self.assertEqual(codecs.decode(b"abc", "ascii", "strict"), "abc")
        self.assertRaises(UnicodeDecodeError, codecs.decode, b"abc\xff", "ascii")
        self.assertRaises(UnicodeDecodeError, codecs.decode, b"abc\xff", "ascii", "strict")
        self.assertEqual(codecs.decode(b"abc\xff", "ascii", "ignore"), "abc")
        self.assertEqual(codecs.decode(b"abc\xff", "ascii", "replace"), "abc?")
        self.assertEqual(codecs.decode
