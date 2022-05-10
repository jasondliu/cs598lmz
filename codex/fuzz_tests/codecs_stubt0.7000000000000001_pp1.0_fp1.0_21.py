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

    def test_encode(self):
        self.assertEqual(b'abcd', "abcd".encode("ascii"))
        self.assertEqual(b'abcd', "abcd".encode("ascii", "replace"))
        self.assertEqual(b'?bcd', "ab\x80d".encode("ascii", "replace"))
        self.assertEqual(b'ab\x80d', "ab\x80d".encode("ascii", "backslashreplace"))
        self.assertEqual(b'ab\x80d', "ab\x80d".encode("ascii", "xmlcharrefreplace"))
        self.assertRaises(UnicodeError, "ab\x80d".encode, "ascii", "strict")
        self.assertRaises(TypeError, "abcd".encode, "ascii", errors="add_one_codepoint")
        self.assertRaises(TypeError, "
