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

class CodecTest(unittest.TestCase):
    def test_utf_8_decode(self):
        self.assertEqual("\u20ac", '\xc2\xac'.decode("utf-8"))
        self.assertEqual("\u20ac", '\xe2\x82\xac'.decode("utf-8"))
        self.assertEqual("\U0001d11e", '\xf0\x9d\x84\x9e'.decode("utf-8"))
        self.assertRaises(UnicodeDecodeError, '\xc2'.decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, '\xe2\x82'.decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, '\xf0\x9d\x84'.decode, "utf-8")
        self.assertEqual("\u20ac", '\xc2\xc2\xac'.decode("utf-8", "replace"))
        self
