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

# This tests that the codecs module correctly handles
# the case where an error handler returns a tuple of
# the replacement string and the index to continue from.

class TestCodecs(unittest.TestCase):
    def test_utf8_error_handler(self):
        # Test the UTF-8 codec with an error handler that just
        # adds a single byte to the end of the string.
        s = b'\xff'
        self.assertEqual(s.decode('utf-8', 'add_one_codepoint'), '\ufffd')
        self.assertEqual(s.decode('utf-8', 'add_utf16_bytes'), '\ufffdb')
        self.assertEqual(s.decode('utf-8', 'add_utf32_bytes'), '\ufffdbcd')

    def test_utf16_error_handler(self):
        # Test the UTF-16 codec with an error handler that just
        # adds a single byte to the end of the string.
        s = b'\xff\xfe'
        self
