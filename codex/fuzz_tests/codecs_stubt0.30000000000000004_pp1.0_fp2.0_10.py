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

class Test_UTF16(unittest.TestCase):
    def test_utf16_decode_errors(self):
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff',
                          'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff\xff',
                          'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff\xff',
                          'strict', False)
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff\xff',
                          'replace', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode, b'\xff\xff',
                          'replace', False)
        self.assertRaises(UnicodeDecodeError, codecs.utf_16_decode
