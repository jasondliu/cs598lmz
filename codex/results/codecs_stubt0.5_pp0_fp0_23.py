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

    def test_ascii_decode(self):
        self.assertEqual(codecs.ascii_decode(b"abc"), ("abc", 3))
        self.assertEqual(codecs.ascii_decode(b"abc\xff"), ("abc\ufffd", 4))
        self.assertRaises(UnicodeDecodeError, codecs.ascii_decode, b"abc\xff", "strict")
        self.assertRaises(UnicodeDecodeError, codecs.ascii_decode, b"abc\xff", "replace", True)
        self.assertRaises(UnicodeDecodeError, codecs.ascii_decode, b"abc\xff", "replace", False)
        self.assertEqual(codecs.ascii_decode(b"abc\xff", "ignore"), ("abc", 4))
        self.assertEqual(codecs.ascii_decode(b"abc\xff",
