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

class TestUnicodeDecodeError(unittest.TestCase):

    def test_init(self):
        self.assertRaises(TypeError, codecs.UnicodeDecodeError)
        self.assertRaises(TypeError, codecs.UnicodeDecodeError, "", b"", -1, -1, "")
        self.assertRaises(TypeError, codecs.UnicodeDecodeError, "", b"", 1.0, 1.0, "")
        self.assertRaises(TypeError, codecs.UnicodeDecodeError, "", b"", 1, 1.0, "")
        self.assertRaises(TypeError, codecs.UnicodeDecodeError, "", b"", 1, 1, 1)
        self.assertRaises(TypeError, codecs.UnicodeDecodeError, "", b"", 1, 1, "", 1)
        self.assertRaises(TypeError, codecs.UnicodeDecodeError, "", b"", 1, 1, "", "")
        self
