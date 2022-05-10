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


class test_encode_codec(unittest.TestCase):

    def test_ascii(self):
        # test ascii character
        self.assertEqual(b'hello', b'hello'.decode('ascii'))
        self.assertEqual(b'x', b'x'.decode('ascii'))
        #self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'ascii')
        self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'ascii', 'strict')
        self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'ascii', 'ignore')
        self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'ascii', 'replace')
        self.assertEqual(b'x', b'\xff'.decode('ascii', 'add_one_codepoint'))
        self.assertRaises(UnicodeDecode
