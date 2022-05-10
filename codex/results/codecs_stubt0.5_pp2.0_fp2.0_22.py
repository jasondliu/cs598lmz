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

class TestCodecs(unittest.TestCase):

    def test_str_decode(self):
        self.assertEqual("abc".decode("utf-8"), u"abc")
        self.assertEqual("abc".decode("utf-8", "strict"), u"abc")
        self.assertEqual("abc".decode("utf-8", "ignore"), u"abc")
        self.assertEqual("abc".decode("utf-8", "replace"), u"abc")
        self.assertEqual("abc".decode("utf-8", "add_one_codepoint"), u"aabc")
        self.assertEqual("abc".decode("utf-8", "add_utf16_bytes"), u"aabc")
        self.assertEqual("abc".decode("utf-8", "add_utf32_bytes"), u"aabc")

        self.assertRaises(UnicodeDecodeError, "abc".decode, "ascii")
        self.assertRaises(UnicodeDecodeError, "abc
