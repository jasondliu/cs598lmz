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

    def test_utf8_decoder(self):
        # Test UTF-8 decoder
        utf8_decoder = codecs.getdecoder('utf-8')
        self.assertEqual(utf8_decoder(b'abc'), ('abc', 3))
        self.assertEqual(utf8_decoder(b'\xe4\xbd\xa0'), ('\u4f60', 3))
        self.assertEqual(utf8_decoder(b'\xe4\xbd\xa0\xe5\xa5\xbd'),
                         ('\u4f60\u597d', 6))
        self.assertEqual(utf8_decoder(b'\xe4\xbd'), ('\ufffd', 1))
        self.assertEqual(utf8_decoder(b'\xe4\xbd', 'strict'),
                         (u'\ufffd', 1))
        self.assertRaises(UnicodeDecodeError, utf8_decoder,
