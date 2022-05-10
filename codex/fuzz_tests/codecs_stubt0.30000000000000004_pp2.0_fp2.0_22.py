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
        self.assertRaises(TypeError, codecs.register_error, 42)
        self.assertRaises(TypeError, codecs.register_error, "strict")
        self.assertRaises(TypeError, codecs.register_error, "replace", 42)

    def test_strict(self):
        self.assertRaises(UnicodeDecodeError, "\xff".decode, "ascii", "strict")
        self.assertRaises(UnicodeEncodeError, "\u0100".encode, "ascii", "strict")

    def test_ignore(self):
        self.assertEqual("\xff".decode("ascii", "ignore"), "")
        self.assertEqual("\u0100".encode("ascii", "ignore"), "")

    def test_replace(self):
        self.assertEqual("\xff".decode("ascii", "replace"), "\ufffd")
        self
