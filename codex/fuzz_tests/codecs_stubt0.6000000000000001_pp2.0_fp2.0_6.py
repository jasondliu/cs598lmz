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

class DecodeTest(unittest.TestCase):
    def test_utf8(self):
        self.assertEqual(b"\xed\xa0\x80".decode("utf-8", "add_one_codepoint"), u"\ud800")
        self.assertEqual(b"\xed\xa0\x80\xed\xb0\x80".decode("utf-8", "add_one_codepoint"), u"\ud800\udc00")
        self.assertEqual(b"\xed\xa0\x80\xed\xb0\x80".decode("utf-8", "add_utf16_bytes"), u"\ud800\udc00")
        self.assertEqual(b"\xf0\x90\x80\x80\xf0\x90\x80\x80".decode("utf-8", "add_utf32_bytes"), u"\U00010000\U00010000")

    def test_utf16(self):
        self.assertEqual(b
