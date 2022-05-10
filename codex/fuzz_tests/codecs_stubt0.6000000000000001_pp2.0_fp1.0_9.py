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

    def test_decode(self):
        self.assertEqual("abcde", "abcde".decode("ascii"))
        self.assertEqual("abcde", "abcde".decode("ascii", "strict"))
        self.assertEqual("abcde", "abcde".decode("ascii", "ignore"))
        self.assertEqual("abcde", "abcde".decode("ascii", "replace"))
        self.assertEqual("abcdexx", "abcde\uFFFE".decode("ascii", "replace"))
        self.assertEqual("abcdexx", "abcde\uFFFE".decode("ascii", "xmlcharrefreplace"))
        self.assertEqual("abcde", "abcde\uFFFE".decode("ascii", "ignore"))
        self.assertRaises(UnicodeDecodeError, "abcde\uFFFE".decode, "ascii", "strict")
        self
