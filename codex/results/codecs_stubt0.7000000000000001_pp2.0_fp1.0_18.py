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
    def test_encode(self):
        # surrogates
        self.assertRaises(UnicodeEncodeError,
                          "abc\ud800".encode, "utf-16")
        self.assertEqual("abc\ud800".encode("utf-16", "ignore"),
                         b'\xff\xfea\x00b\x00c\x00\x00\x00')
        self.assertEqual("abc\ud800".encode("utf-16", "replace"),
                         b'\xff\xfea\x00b\x00c\x00\xff\xfd\x00')
        self.assertEqual("abc\ud800".encode("utf-16", "add_one_codepoint"),
                         b'\xff\xfea\x00b\x00c\x00\x00\x00a\x00')
        self.assertEqual("abc\ud800".encode("utf-16", "add_utf16_bytes"),

