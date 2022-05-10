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

class CodecsModuleTest(unittest.TestCase):

    # error callback handling
    def test_errorcallback_decoding(self):
        self.assertRaises(UnicodeDecodeError, u'\xff'.decode, 'ascii')
        self.assertEqual('\xe0\u20ac'.decode('ascii', 'add_one_codepoint'),
                         '\xe0a')
        self.assertRaises(UnicodeDecodeError, b'\xff\xff'.decode, 'ascii')
        self.assertEqual(b'\x00\xff'.decode('utf-16'), '\ufffd\ufffd')
        self.assertEqual(b'\x00\xff'.decode('utf-16', 'add_utf16_bytes'),
                         '\ufffd\x00\x00ab\ufffd')

    def test_errorcallback_encoding(self):
        self.assertRaises(UnicodeEncodeError, '\u20ac'.encode, 'ascii')
       
