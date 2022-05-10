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

class TestUTF8(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual(b"a\xef\xbf\xbd".decode("utf-8", "add_one_codepoint"), "a\ufffd")

    def test_add_utf16_bytes(self):
        self.assertEqual(b"a\xef\xbf".decode("utf-8", "add_utf16_bytes"), "a\ufffd\ufffd")

    def test_add_utf32_bytes(self):
        self.assertEqual(b"a\xef\xbf\xbd".decode("utf-8", "add_utf32_bytes"), "a\ufffd\ufffd\ufffd")

    def test_surrogates(self):
        self.assertEqual(b"a\xed\xa0\x80\xed\xbf\xbf".decode("utf-8", "replace"), "a\ufffd\ufffd")
        self.assert
