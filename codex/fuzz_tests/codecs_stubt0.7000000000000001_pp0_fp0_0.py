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

class CodecUTF32Test(unittest.TestCase):
    encoding = 'utf-32'
    test_string = '\u20ac\u8000\u10400'

    def test_encode(self):
        self.assertEqual(self.test_string.encode(self.encoding),
                         b'\xff\xfe\x00\x00\xe2\x82\xac\x00\x00\x80\x00'
                         b'\x00\x00\x01\xd0\x80\x00')
        self.assertEqual(self.test_string.encode(self.encoding, 'strict'),
                         b'\xff\xfe\x00\x00\xe2\x82\xac\x00\x00\x80\x00'
                         b'\x00\x00\x01\xd0\x80\x00')
        self.assertEqual(self.test_string.encode(self.encoding, 'ignore'),
                         b'\xff\xfe
