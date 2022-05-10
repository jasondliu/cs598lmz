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

    def test_basics(self):
        utf8_decoder = codecs.getdecoder("utf8")
        utf8_encoder = codecs.getencoder("utf8")

        # check that encode() is the inverse of decode()
        s = "abc123"
        self.assertEqual(s, utf8_decoder(utf8_encoder(s)[0])[0])
        self.assertEqual(s, utf8_decoder(utf8_encoder(s, "xmlcharrefreplace")[0])[0])
        self.assertEqual(s, utf8_decoder(utf8_encoder(s, "strict")[0])[0])
        self.assertEqual(s, utf8_decoder(utf8_encoder(s, "ignore")[0])[0])

        # check that encode() raises an error given the wrong kind of input
        self.assertRaises(TypeError, utf8_encoder, u
