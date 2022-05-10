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

class TestErrorHandler(unittest.TestCase):

    def test_replace(self):
        s = codecs.escape_decode(b'"\\n\\r\\t\\f\\b\\a\\\\"')[0]
        self.assertEqual(s, b'\n\r\t\f\b\a\\"')
        self.assertRaises(UnicodeDecodeError,
                          codecs.escape_decode, b'"\\z"')
        # Issue #19266
        s = codecs.escape_decode(b'"\\z"', 'backslashreplace')[0]
        self.assertEqual(s, b'\\z')
        s = codecs.escape_decode(b'"\\z"', 'backslashreplace')[0]
        self.assertEqual(s, b'\\z')
        s = codecs.escape_decode(b'"\\z\\x"', 'backslashreplace')[0]
        self.assertEqual(s, b'\\x')
        s = codecs
