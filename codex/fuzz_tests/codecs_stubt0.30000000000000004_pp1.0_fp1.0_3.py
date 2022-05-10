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

class TestUnicodeDecodeError(unittest.TestCase):

    def test_add_one_codepoint(self):
        # Test the add_one_codepoint error handler
        s = b'\xff'
        self.assertRaises(UnicodeDecodeError, s.decode, 'ascii')
        self.assertEqual(s.decode('ascii', 'add_one_codepoint'), 'a\ufffd')

    def test_add_utf16_bytes(self):
        # Test the add_utf16_bytes error handler
        s = b'\xff'
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-16')
        self.assertEqual(s.decode('utf-16', 'add_utf16_bytes'), 'a\ufffd')

    def test_add_utf32_bytes(self):
        # Test the add_utf32_bytes error handler
        s = b'\xff'
        self.assertRaises(UnicodeDecodeError
