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

class TestBadDecode(unittest.TestCase):
    def test_utf8_decode_error(self):
        for encoding in (
            "utf8",
            "utf-8"
        ):
            self.assertEqual(u"\ud800a",
                "\ud800".decode(encoding, "add_one_codepoint"))
            self.assertEqual(u"a\ud800",
                "\ud800".decode(encoding, "add_one_codepoint"))
            self.assertEqual(u"\ud800\ufffd",
                "\ud800".decode(encoding, "replace"))
            self.assertEqual(u"\ud800\ufffd",
                "\ud800".decode(encoding, "ignore"))
            self.assertEqual(u"\ud800",
                "\ud800".decode(encoding, "xmlcharrefreplace"))
            self.assertEqual(u"\ud800",
                "\ud800".decode(encoding, "backslashreplace"))

    def
