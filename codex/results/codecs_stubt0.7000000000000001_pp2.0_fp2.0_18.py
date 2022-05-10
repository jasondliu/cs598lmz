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

    def test_decoding(self):
        self.assertEqual(codecs.decode("abc\xff", "utf-8", "add_one_codepoint"), "aabc\ufffd")
        self.assertEqual(codecs.decode("abc\xff", "utf-8", "ignore"), "abc")
        self.assertEqual(codecs.decode("abc\xff", "utf-8", "replace"), "abc\ufffd")
        self.assertEqual(codecs.decode("abc\xff", "utf-8", "strict"), None)
        self.assertEqual(codecs.decode("abc\xff", "utf-8", "surrogateescape"), "abc\xff")

    def test_encoding(self):
        self.assertEqual(codecs.encode("a\u1234", "utf-8", "add_utf8_bytes"), b"ab")
        self.assertEqual(codecs.encode("
