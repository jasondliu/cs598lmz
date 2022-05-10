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

class Test_Surrogates(unittest.TestCase):

    def test_encode_surrogate_pair(self):
        # Surrogate pair and non-BMP character
        self.assertEqual(b'\xed\xa0\x80\xed\xb0\x80',
            '\ud800\udc00'.encode('utf-16-be'))
        self.assertEqual(b'\xed\xb0\x80\xed\xa0\x80',
            '\udc00\ud800'.encode('utf-16-be'))

        # Lone high surrogate
        self.assertEqual(b'\xed\xa0\x80', '\ud800'.encode('utf-16-be',
            'surrogatepass'))
        self.assertEqual(b'\xed\xa0\x80', '\ud800'.encode('utf-16-be',
            'surrogateescape'))
        self.assertRaises(UnicodeEncodeError, '\ud
