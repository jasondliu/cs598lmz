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

from test import support

class TestBase:
    encodings = []
    strings = ['[\x00-\x7f]']

    def test_basic(self):
        for encoding in self.encodings:
            for string in self.strings:
                self.assertEqual(string.encode(encoding),
                                 codecs.escape_decode(string))

    def test_errors(self):
        for encoding in self.encodings:
            for string in self.strings:
                # Test default error handler
                self.assertRaises(UnicodeEncodeError, string.encode, encoding, 'strict')
                # Test custom error handler
                self.assertEqual(string.encode(encoding, 'add_one_codepoint'),
                                 codecs.escape_decode(string))

class TestUTF8(TestBase, unittest.TestCase):
    encodings = ['utf-8']
    strings = ['surrogates:\ud800\udc00\ud800\ud800\udc00\ud
