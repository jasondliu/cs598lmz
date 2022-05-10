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
        self.assertRaises(TypeError, codecs.register_error, None, None)
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", None)
        self.assertRaises(TypeError, codecs.register_error, None, add_one_codepoint)
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", add_one_codepoint, None)
        self.assertRaises(ValueError, codecs.register_error, "", add_one_codepoint)
        self.assertRaises(ValueError, codecs.register_error, "a", add_one_codepoint)
        self.assertRaises(ValueError, codecs.register_error, "add_one_codepoint", add_one_codepoint, 42)

    def test_lookup_error(self):
        self.assertRaises
