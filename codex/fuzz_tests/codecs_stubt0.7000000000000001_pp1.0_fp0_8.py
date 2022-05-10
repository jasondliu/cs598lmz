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

class TestIncrementalDecoder(unittest.TestCase):

    def setUp(self):
        self.expect_error = False
        self.src_encoding = 'ascii'
        self.tgt_encoding = 'ascii'

    def tearDown(self):
        if self.expect_error:
            pass
        else:
            self.assertEqual(self.decoder.decode(b"", True), "")
            self.assertEqual(self.encoder.encode(""), b"")

    def feed_decoder(self, bytes, expected=None, errors="strict"):
        if expected is None:
            expected = bytes.decode(self.src_encoding, errors)
        self.assertEqual(self.decoder.decode(bytes, False), expected)

    def feed_encoder(self, string, expected=None, errors="strict"):
        if expected is None:
            expected = string.encode(self.tgt_encoding, errors)
        self.assertEqual
