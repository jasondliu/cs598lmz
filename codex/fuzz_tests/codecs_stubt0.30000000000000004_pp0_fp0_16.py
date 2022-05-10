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
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff', 'strict', False)
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff', 'strict', False)
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff\xff', 'strict', True)
        self.assertRaises(UnicodeDecodeError, codecs.utf_8_decode, b'\xff\xff\xff', 'strict', False)
