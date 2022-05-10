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

class TestCase(unittest.TestCase):
    # Test UnicodeError handling
    def test_unicode_error(self):
        #Test UnicodeEncodeError handling
        self.assertEqual(b"abc\uffff".decode("ascii", "add_one_codepoint"), "abc\uffffa")
        self.assertEqual(b"abc\xff".decode("ascii", "add_one_codepoint"), "abc\xffa")
        self.assertEqual(b"abc\xff\xff".decode("ascii", "add_one_codepoint"), "abc\xff\xffa")
        self.assertEqual(b"abc\xff\xff\xff".decode("ascii", "add_one_codepoint"), "abc\xff\xff\xffa")
        self.assertEqual(b"abc\xff\xff\xff\xff".decode("ascii", "add_one_codepoint"), "abc\xff\xff\xff\xffa")
        self.assertEqual(
