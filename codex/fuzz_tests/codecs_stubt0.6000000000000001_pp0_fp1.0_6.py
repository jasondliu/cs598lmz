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

class TestUnicodeError(unittest.TestCase):

    def test_str_error(self):
        self.assertEqual(str(UnicodeError(42, 42, 43, "message")),
                         "message")
        self.assertEqual(str(UnicodeEncodeError(42, 42, 43, 44, "message")),
                         "message")
        self.assertEqual(str(UnicodeDecodeError(42, 42, 43, 44, "message")),
                         "message")
        self.assertEqual(str(UnicodeTranslateError(42, 42, 43, 44, "message")),
                         "message")

    def test_repr_error(self):
        self.assertEqual(repr(UnicodeError(42, 42, 43, "message")),
                         "UnicodeError(42, 42, 43, 'message')")
        self.assertEqual(repr(UnicodeEncodeError(42, 42, 43, 44, "message")),
                         "UnicodeEncodeError(
