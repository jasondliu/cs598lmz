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

class TestUTF16(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(u"abc", "\xff\xfea\x00b\x00c\x00".decode("utf-16"))
        self.assertEqual(u"abc", "\xfe\xff\x00a\x00b\x00c".decode("utf-16"))
        self.assertEqual(u"abc", "\x00a\x00b\x00c".decode("utf-16-le"))
        self.assertEqual(u"abc", "\x00a\x00b\x00c".decode("utf-16-be"))
        self.assertEqual(u"abc", "\xff\xfea\x00b\x00c\x00".decode("utf-16-be"))

        self.assertRaises(UnicodeDecodeError, "\xff\xfea\x00b\x00c".decode, "utf-16")

        self.assertEqual(u"abc\
