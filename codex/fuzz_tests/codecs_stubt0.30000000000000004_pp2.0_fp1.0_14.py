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

# The following tests are written to check that the codecs module
# behaves as expected.

# Test the UTF-8 codec

class TestUTF8(unittest.TestCase):

    def test_utf8(self):
        self.assertEqual(codecs.utf_8_encode(u"abc")[0], b"abc")
        self.assertEqual(codecs.utf_8_encode(u"abc", "strict")[0], b"abc")
        self.assertEqual(codecs.utf_8_encode(u"abc", "ignore")[0], b"abc")
        self.assertEqual(codecs.utf_8_encode(u"abc", "replace")[0], b"abc")
        self.assertEqual(codecs.utf_8_encode(u"abc", "xmlcharrefreplace")[0],
                         b"abc")
        self.assertEqual(codecs.utf_8_encode(u"abc", "backslashreplace")[0],

