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

class BaseTest(unittest.TestCase):
    encoding = None
    exceptions = None

    def test_decoding_error(self):
        if self.exceptions is None:
            self.assertRaises(UnicodeDecodeError,
                              codecs.decode, b'\xff', self.encoding)
        else:
            self.assertEqual(codecs.decode(b'\xff', self.encoding,
                                           self.exceptions), 'a')

    def test_encoding_error(self):
        if self.exceptions is None:
            self.assertRaises(UnicodeEncodeError,
                              codecs.encode, '\udc80', self.encoding)
        else:
            self.assertEqual(codecs.encode('\udc80', self.encoding,
                                           self.exceptions), b'ab')

class TestUTF8(BaseTest):
    encoding = 'utf-8'
    exceptions = 'add_one_codepoint'

class Test
