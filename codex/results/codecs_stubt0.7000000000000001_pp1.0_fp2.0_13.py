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

class CodecTest(unittest.TestCase):
    def assertEqual2(self, x, y, msg=None):
        self.assertEqual(x, y, msg)
        self.assertEqual(type(x), type(y), msg)

    def test_utf16_error_handler(self):
        # test error handling in UTF-16
        self.assertEqual(b'\xff\xfea\x00'.decode('utf-16', errors='add_one_codepoint'),
                         'a')
        self.assertEqual(b'\xff\xfea\x00'.decode('utf-16', errors='add_utf16_bytes'),
                         'aa')
        self.assertEqual(b'\xff\xfea\x00'.decode('utf-16', errors='add_utf32_bytes'),
                         '\U00010203a')

    def test_unicodeescape_errors(self):
        # test error handlers for unicode-escape
        self.assertEqual(b'\xff\xfe
