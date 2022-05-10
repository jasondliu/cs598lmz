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

class UnicodeDecodeErrorTest(unittest.TestCase):
    def test_bad_decode(self):
        err = codecs.lookup_error("add_one_codepoint")
        self.assertEqual(err("abc", 1, 2, "foo"),
            (u"a", 1))

    def test_bad_decode_utf16(self):
        err = codecs.lookup_error("add_utf16_bytes")
        self.assertEqual(err("abc", 1, 2, "foo"),
            (u"ab", 1))

    def test_bad_decode_utf32(self):
        err = codecs.lookup_error("add_utf32_bytes")
        self.assertEqual(err("abc", 1, 2, "foo"),
            (u"abcd", 1))

    def test_constructor(self):
        exc = UnicodeDecodeError("add_one_codepoint", b"abc", 1, 2, "foo")
        self.assertEqual(exc.encoding, "add_
