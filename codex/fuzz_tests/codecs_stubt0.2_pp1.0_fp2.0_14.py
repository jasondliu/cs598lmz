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
    def test_utf8_decode_errors(self):
        # Test UTF-8 decoding errors
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, '\xff\xff'.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, '\xff\xff\xff'.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, '\xff\xff\xff\xff'.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, '\xff\xff\xff\xff\xff'.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, '\xc0\x80'.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, '\xc1\x80'.decode, 'utf-8')
