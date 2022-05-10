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
    def test_add_one_codepoint(self):
        self.assertEqual("ab", "a".decode("ascii", "add_one_codepoint"))
        self.assertEqual("ab\u1234", "\u1234".decode("utf-8", "add_one_codepoint"))
        self.assertEqual("ab\u1234", "\u1234".decode("utf-16", "add_one_codepoint"))
        self.assertEqual("ab\u1234\u5678", "\u1234\u5678".decode("utf-32", "add_one_codepoint"))

    def test_add_utf16_bytes(self):
        self.assertEqual("ab", "a".decode("ascii", "add_utf16_bytes"))
        self.assertEqual("ab\u1234", "\u1234".decode("utf-8", "add_utf16_bytes"))
        self.assertEqual("
