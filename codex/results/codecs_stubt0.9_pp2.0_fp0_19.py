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

class IncrementalEncoderTest(unittest.TestCase):

    def test_error_handling(self):
        def test_encoder(name, input, errors):
            encoder = codecs.getincrementalencoder(name)(errors=errors)
            out = encoder.encode(input)
            out += encoder.encode("", True)
            return out

        self.assertEqual(test_encoder("ascii", "\x80", "ignore"), b"")
        self.assertEqual(test_encoder("ascii", "\x80", "replace"), b"?",)
        self.assertEqual(test_encoder("ascii", "\x80", "xmlcharrefreplace"),
                          b"&#128;")
        self.assertRaises(UnicodeEncodeError, test_encoder, "ascii", "\x80",
                          "strict")
        self.assertRaises(UnicodeEncodeError, test_encoder, "ascii", "\x80",
                          "strict")
