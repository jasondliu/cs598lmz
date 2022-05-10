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

class TestErrorHandling(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual("a\x80a", "ab".decode("ascii", "add_one_codepoint"))
        self.assertEqual("a\x80a", "ab".decode("iso-8859-1", "add_one_codepoint"))

    def test_add_utf16_bytes(self):
        self.assertEqual("a\ud800a", "ab".decode("utf-16-be", "add_utf16_bytes"))
        self.assertEqual("a\ud800a", "ab".decode("utf-16-le", "add_utf16_bytes"))

    def test_add_utf32_bytes(self):
        self.assertEqual("a\ud800a", "ab".decode("utf-32-be", "add_utf32_bytes"))
        self.assertEqual("a\ud800a", "ab".decode("utf-32-le",
