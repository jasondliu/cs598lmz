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

class CodecsModuleTest(unittest.TestCase):

    def test_register_error(self):
        self.assertRaises(TypeError, codecs.register_error, 42)
        self.assertRaises(TypeError, codecs.register_error, "strict", 42)
        self.assertRaises(LookupError, codecs.register_error, "__spam__")
        self.assertRaises(TypeError, codecs.register_error, "strict", lambda x: x)
        self.assertRaises(TypeError, codecs.register_error, "strict",
                          lambda x: x, 42)

    def test_lookup_error(self):
        self.assertRaises(TypeError, codecs.lookup_error, 42)
        self.assertRaises(LookupError, codecs.lookup_error, "__spam__")
        self.assertRaises(TypeError, codecs.lookup_error, "strict", 42)

    def test_strict_errors(self):
        self.assert
