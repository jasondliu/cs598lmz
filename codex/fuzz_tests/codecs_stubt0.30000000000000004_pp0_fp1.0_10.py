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
        # utf-8
        self.assertEqual(codecs.utf_8_decode(b"abc"), ("abc", 3))
        self.assertEqual(codecs.utf_8_decode(b"abc\xff"), ("abc\ufffd", 4))
        self.assertEqual(codecs.utf_8_decode(b"abc\xc1\xbf\xff"), ("abc\ufffd\ufffd", 6))
        self.assertEqual(codecs.utf_8_decode(b"\xff"), ("\ufffd", 1))
        self.assertEqual(codecs.utf_8_decode(b"\xc1\xbf"), ("\ufffd", 2))
        self.assertEqual(codecs.utf_8_decode(b"\xf4\x90\x80\x80"), ("\U0010ffff", 4))
        self.assertRaises(Un
