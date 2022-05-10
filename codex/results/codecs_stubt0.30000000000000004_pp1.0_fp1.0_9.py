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

    def test_utf8_decode(self):
        self.assertEqual(b"\x00".decode("utf-8"), "\x00")
        self.assertEqual(b"\xc2\x80".decode("utf-8"), "\x80")
        self.assertEqual(b"\xe0\xa0\x80".decode("utf-8"), "\u0800")
        self.assertEqual(b"\xf0\x90\x80\x80".decode("utf-8"), "\U00010000")

        self.assertRaises(UnicodeDecodeError, b"\x80".decode, "utf-8")
        self.assertRaises(UnicodeDecodeError, b"\x80".decode, "utf-8", "strict")
        self.assertRaises(UnicodeDecodeError, b"\x80".decode, "utf-8", "ignore")
        self.assertRaises(UnicodeDecodeError
