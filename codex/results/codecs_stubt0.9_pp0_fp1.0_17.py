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

class UnicodeErrorTests(unittest.TestCase):

    def test_decode_error_endofdata(self):
        for encoding in ('ascii', 'latin-1', 'utf-8'):
            self.assertEqual("", "\0".encode(encoding))

        for encoding in ('utf-7', 'utf-32', 'utf-16'):
            self.assertRaises(UnicodeError, "\0".encode, encoding)

    def test_decode_error_truncated_data(self):
        for encoding in ('ascii', 'latin-1'):
            self.assertEqual("abc", "abc\0".encode(encoding))
            self.assertRaises(UnicodeError, "abc".encode, encoding)

        for encoding in ("utf-7", "utf-16", "utf-32"):
            self.assertRaises(UnicodeError, "abc".encode, encoding)
            self.assertRaises(UnicodeError, "abc\0".encode, encoding)
