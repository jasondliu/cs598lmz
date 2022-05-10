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
    def test_register_error(self):
        # Testing the codecs.register_error function
        # First we need a codec which can raise errors
        self.assertRaises(UnicodeError, "\u3042".encode, "ascii")
        # Now we register an error handler
        codecs.register_error("test.codec", lambda x: ("", x.start))
        # Now the encoding should succeed
        self.assertEqual("\u3042".encode("ascii", "test.codec"), "")
        # We can also register an error handler for a specific exception
        codecs.register_error("test.codec", lambda x: ("", x.start),
                              UnicodeEncodeError)
        # Now the encoding should succeed
        self.assertEqual("\u3042".encode("ascii", "test.codec"), "")
        # But it should fail for other exceptions
        self.assertRaises(UnicodeError, "\u3042".encode
