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
    def test_utf8_errors(self):
        # Test UTF-8 error handlers
        self.assertEqual(codecs.utf_8_decode(b'\xff', "replace")[0], '\ufffd')
        self.assertEqual(codecs.utf_8_decode(b'\xff', "ignore")[0], '')
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff',
                          "strict")
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff',
                          "add_one_codepoint")
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff',
                          "add_utf16_bytes")
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff',
                
