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

class Test_UTF8(unittest.TestCase):
    def test_decoder(self):
        self.assertEqual("\uFFFD\uFFFD", "ab\x80".decode("utf-8", "replace"))
        self.assertEqual("\uefbfbd\uFFFD", "ab\xc0\x80".decode("utf-8", "replace"))
        self.assertEqual("a\uefbfbd\uFFFD", "ab\xc1\x80".decode("utf-8", "replace"))
        self.assertEqual("\uefbfbd\uFFFD\uefbfbd", "\xc0\xaf".decode("utf-8", "replace"))
        self.assertEqual("\uefbfbd\uFFFD\uefbfbd", "\xc1\x2f".decode("utf-8", "replace"))
        self.assertEqual("\uefbfbd\uFFFD\uefbfbd", "\xe0\x80\xaf".decode("utf-8", "
