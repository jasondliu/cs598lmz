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

    def test_utf8_decode(self):
        self.assertEqual(codecs.utf_8_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.utf_8_decode(b'abc\xff'), ('abc\ufffd', 4))
        self.assertEqual(codecs.utf_8_decode(b'abc\xc1\x80'), ('abc\u0800', 4))
        self.assertEqual(codecs.utf_8_decode(b'abc\xe0\x80\x80'), ('abc\u8000', 4))
        self.assertEqual(codecs.utf_8_decode(b'abc\xf0\x80\x80\x80'), ('abc\U00010000', 4))
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'abc\xf8\x80\x80\x80\x80')
