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

class TestErrorHandlers(unittest.TestCase):

    def test_string_decode_error(self):
        for error in ('strict', 'replace', 'ignore'):
            self.assertRaises(UnicodeDecodeError,
                              '\xc0'.encode, 'ascii', error)
        self.assertEqual('a'.encode('ascii', 'add_one_codepoint'), b'a')
        self.assertEqual('\xc0'.encode('ascii', 'backslashreplace'), b'\\xc0')

    def test_string_encode_error(self):
        for error in ('strict', 'replace', 'ignore'):
            self.assertRaises(UnicodeEncodeError,
                              '\ud800'.encode, 'ascii', error)
        self.assertEqual('\ud800'.encode('ascii', 'add_one_codepoint'), b'a')
        self.assertEqual('\ud800'.encode('ascii', 'back
