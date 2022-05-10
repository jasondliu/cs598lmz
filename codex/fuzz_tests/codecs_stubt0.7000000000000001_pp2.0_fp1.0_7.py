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
        self.assertEqual("a\ufffe", "a\ufffe".decode("utf-8", "add_one_codepoint"))
        self.assertEqual("a\ufffeb", "a\ufffe".decode("utf-16", "add_one_codepoint"))
        self.assertEqual("a\ufffebcd", "a\ufffe".decode("utf-32", "add_one_codepoint"))

    def test_add_utf16_bytes(self):
        self.assertEqual("a\ufffeb", "a\ufffe".decode("utf-8", "add_utf16_bytes"))

    def test_add_utf32_bytes(self):
        self.assertEqual("a\ufffebcd", "a\ufffe".decode("utf-8", "add_utf32_bytes"))

class TestEncode(unittest.TestCase):
    def test_
