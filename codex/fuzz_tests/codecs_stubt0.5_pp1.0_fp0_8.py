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
    def test_utf8_surrogates(self):
        # Test that we raise the correct exception for surrogates
        self.assertRaises(UnicodeError, '\ud800'.encode, 'utf-8')
        self.assertRaises(UnicodeError, '\udc00'.encode, 'utf-8')
        self.assertRaises(UnicodeError, '\ud800\udc00'.encode, 'utf-8')
        self.assertRaises(UnicodeError, '\udbff\udfff'.encode, 'utf-8')

    def test_utf8_errors(self):
        # Test that we raise the correct exception for various errors
        self.assertRaises(UnicodeError, '\xff'.encode, 'utf-8')
        self.assertRaises(UnicodeError, '\xff'.encode, 'utf-8', 'strict')
        self.assertRaises(UnicodeError, '\xff'.encode, 'utf
