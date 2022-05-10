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

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_decode(b'\x00\x7f'), ('\x00\x7f', 2))
        self.assertEqual(codecs.utf_8_decode(b'\xc2\x80\xdf\xbf'), ('\x80\u07ff', 4))
        self.assertEqual(codecs.utf_8_decode(b'\xe0\xa0\x80\xef\xbf\xbf'), ('\u0800\uffff', 6))
        self.assertEqual(codecs.utf_8_decode(b'\xf0\x90\x80\x80\xf4\x8f\xbf\xbf'), ('\U00010000\U0010ffff', 8))
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\x80')
        self.
