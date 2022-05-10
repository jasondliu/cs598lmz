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
        self.assertRaises(TypeError, codecs.register_error,
                          "test", "not callable")
        self.assertRaises(TypeError, codecs.register_error,
                          42, lambda x:x)
        self.assertRaises(LookupError, codecs.register_error,
                          "test", lambda x:x)
        # Check on unknown encoding
        self.assertRaises(LookupError, codecs.register_error,
                          "test", lambda x:x, "__spam__")
        # Check on known encoding
        self.assertRaises(LookupError, codecs.register_error,
                          "test", lambda x:x, "ascii")
        # Check on unknown error handler name
        self.assertRaises(LookupError, codecs.lookup_error,
                          "__spam__")
        # Check on known error handler name
        self.assertEqual(codec
