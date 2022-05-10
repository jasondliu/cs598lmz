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
        self.assertEqual("abc", "abc".decode("ascii"))
        self.assertEqual("abc", "abc".decode("ascii", "strict"))
        self.assertEqual("abc", "abc".decode("ascii", "ignore"))
        self.assertEqual("abc", "abc".decode("ascii", "replace"))
        self.assertEqual("abc", "abc".decode("ascii", "backslashreplace"))
        self.assertEqual("abc", "abc".decode("ascii", "xmlcharrefreplace"))
        self.assertEqual("abc", "abc".decode("ascii", "add_one_codepoint"))
        self.assertEqual("abc", "abc".decode("ascii", "add_utf16_bytes"))
        self.assertEqual("abc", "abc".decode("ascii", "add_utf32_bytes"))

        self.
