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
        self.assertRaises(LookupError, codecs.register_error, "spam")
        self.assertRaises(TypeError, codecs.register_error, "strict", "replace", 42)
        self.assertRaises(TypeError, codecs.register_error, "strict", "replace",
                          lambda x: (u"", x.start+1))
        self.assertRaises(TypeError, codecs.register_error, "strict", "replace",
                          lambda x: (u"", x.start+1, x.end+1))
        self.assertRaises(TypeError, codecs.register_error, "strict", "replace",
                          lambda x: (u"", x.start+1, x.end+1,
