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

    def test_utf8_surrogatepass_handler(self):
        self.assertRaises(UnicodeDecodeError, b'\xed\xa0\x80'.decode, 'utf-8', 'surrogatepass')

    def test_utf8_surrogateescape_handler(self):
        self.assertEqual(b'\xed\xa0\x80'.decode('utf-8', 'surrogateescape'),
                         '\udc00')

    def test_utf8_surrogateescape_encode(self):
        self.assertEqual('\udc00'.encode('utf-8', 'surrogateescape'),
                         b'\xed\xa0\x80')

        self.assertEqual(b'\xed\xa0\x80'.decode('utf-8', 'surrogateescape'),
                         '\udc00')
        self.assertEqual('\udc00'.encode('utf-8', 'surrogateescape
