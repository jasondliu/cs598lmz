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

class TestAsciiDecode(unittest.TestCase):

    def test_ascii_decode(self):
        self.assertEqual(u"abc".encode("ascii", "strict"), b"abc")
        self.assertEqual(u"abc".encode("ascii", "ignore"), b"abc")
        self.assertEqual(u"abc".encode("ascii", "replace"), b"abc")
        self.assertEqual(u"abc".encode("ascii", "xmlcharrefreplace"), b"abc")
        self.assertEqual(u"abc".encode("ascii", "backslashreplace"), b"abc")

        self.assertRaises(UnicodeEncodeError, u"\xe9".encode, "ascii", "strict")

        self.assertEqual(u"\xe9".encode("ascii", "ignore"), b"")
        self.assertEqual(u"\xe9".encode("ascii", "replace"), b"?"
