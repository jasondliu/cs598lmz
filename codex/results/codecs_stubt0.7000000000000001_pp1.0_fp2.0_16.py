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

class TestCharmap(unittest.TestCase):
    def test_encode_decode(self):
        # charmap_encode should not accept unicode strings with surrogates
        self.assertRaises(UnicodeError, '\ud800'.encode, 'charmap')
        self.assertRaises(UnicodeError, '\ud80c'.encode, 'charmap')
        self.assertRaises(UnicodeError, '\udfff'.encode, 'charmap')
        self.assertRaises(UnicodeError, '\ud800\udc00'.encode, 'charmap')
        self.assertRaises(UnicodeError, '\udbff\udfff'.encode, 'charmap')

        # charmap_decode should not accept bytes with surrogates
        self.assertRaises(UnicodeError, b''.decode, 'charmap',
                          'surrogatepass')
        self.assertRaises(UnicodeError, b'\x80'.decode, 'ch
