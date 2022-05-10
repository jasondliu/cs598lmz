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
        utf8 = codecs.getencoder("utf8")
        utf16 = codecs.getencoder("utf16")
        utf32 = codecs.getencoder("utf32")

        self.assertRaises(UnicodeEncodeError, utf8, "caf\uFFFD", "add_one_codepoint")
        self.assertRaises(UnicodeEncodeError, utf16, "caf\uFFFD", "add_one_codepoint")
        self.assertRaises(UnicodeEncodeError, utf32, "caf\uFFFD", "add_one_codepoint")

        self.assertRaises(UnicodeEncodeError, utf8, "caf\uFFFD", "add_utf16_bytes")
        self.assertRaises(UnicodeEncodeError, utf16, "caf\uFFFD", "add_utf16_bytes")
        self
