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

class TestInvalidCodec(unittest.TestCase):
    def test_invalid_codec(self):
        self.assertRaises(LookupError, codecs.getencoder, "invalid")
        self.assertRaises(LookupError, codecs.getdecoder, "invalid")

    def test_invalid_error_handler(self):
        self.assertRaises(LookupError, codecs.register_error, "invalid", add_one_codepoint)

    def test_invalid_encoding(self):
        self.assertRaises(LookupError, codecs.getencoder, "invalid")
        self.assertRaises(LookupError, codecs.getdecoder, "invalid")

    def test_invalid_error_handler(self):
        self.assertRaises(LookupError, codecs.register_error, "invalid", add_one_codepoint)

    def test_invalid_error_handler_utf16(self):
        self.assertRaises(LookupError, codecs.
