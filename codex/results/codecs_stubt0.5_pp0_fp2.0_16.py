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

class TestEncode(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(b"abc", "abc".encode("ascii"))
        self.assertEqual(b"abc", "abc".encode("ascii", "strict"))
        self.assertEqual(b"abc", "abc".encode("ascii", "ignore"))
        self.assertEqual(b"abc", "abc".encode("ascii", "replace"))
        self.assertEqual(b"abc", "abc".encode("ascii", "xmlcharrefreplace"))
        self.assertEqual(b"abc", "abc".encode("ascii", "backslashreplace"))

        self.assertEqual(b"abc", "abc".encode("latin-1"))
        self.assertEqual(b"abc", "abc".encode("latin-1", "strict"))
        self.assertEqual(b"abc", "abc".encode("latin-1", "ignore"))

