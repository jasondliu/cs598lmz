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

class CodecTestCase(unittest.TestCase):
    """A collection of tests for codecs."""

    def test_encode_utf8_surrogates(self):
        # Check that surrogates are correctly encoded
        # by the UTF-8 encoder
        self.assertEqual(codecs.utf_8_encode(u"abc\udc80")[0], b"abc\xed\xb2\x80")

    def test_encode_utf8_error_handling(self):
        # Check that the UTF-8 encoder replace and ignores surrogates
        self.assertEqual(codecs.utf_8_encode(u"abc\udc80", "replace")[0], b"abc?")
        self.assertEqual(codecs.utf_8_encode(u"abc\udc80", "ignore")[0], b"abc")
        self.assertEqual(codecs.utf_8_encode(u"abc\udc80", "surrogatepass")[0], b"abc\
