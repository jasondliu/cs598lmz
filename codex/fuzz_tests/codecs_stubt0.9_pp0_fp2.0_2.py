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


class TestCodecs(unittest.TestCase):
    def test_bad_codecs(self):
        """ Test bad UTF-8 input """

        # Test each possible error handler response
        decoded, bytes_eaten = codecs.utf_8_decode("\x00\xff",
                                                   "add_one_codepoint")
        self.assertEqual(decoded, "a\ufffd")

        decoded, bytes_eaten = codecs.utf_8_decode("\x00\xff",
                                                   "add_utf16_bytes")
        self.assertEqual(decoded, "\ufffdb")

        decoded, bytes_eaten = codecs.utf_8_decode("\x00\xff",
                                                   "add_utf32_bytes")
        self.assertEqual(decoded, "\ufffd\x00bcd")

        decoded, bytes_eaten = codecs.utf_8_decode("\x00\xff", "replace")
        self.assertEqual(decoded,
