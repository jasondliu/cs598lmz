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

    def test_encode_decode(self):
        self.assertEqual(codecs.encode("abc", "ascii"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii", "strict"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii", "ignore"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii", "replace"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii", "xmlcharrefreplace"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii", "backslashreplace"), b"abc")
        self.assertEqual(codecs.encode("abc", "ascii", "namereplace"), b"abc")
        self.assertEqual(codecs.encode("abc", "as
