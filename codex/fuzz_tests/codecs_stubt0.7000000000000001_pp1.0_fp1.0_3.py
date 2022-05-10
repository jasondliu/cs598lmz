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

class Test_Error_Handling(unittest.TestCase):
    def test_codec_lookup_error(self):
        self.assertRaises(LookupError, codecs.lookup, "codecs_error_test")

    def test_strict_errors(self):
        s = "this is a test: \xff\xff"
        self.assertRaises(UnicodeDecodeError, s.decode, "ascii", "strict")
        self.assertRaises(UnicodeEncodeError, s.encode, "ascii", "strict")
        self.assertRaises(UnicodeTranslateError, s.translate, {0xffff: None}, "strict")

    def test_ignore_errors(self):
        s = "this is a test: \xff\xff"
        self.assertEqual(s.decode("ascii", "ignore"), "this is a test: ")
        self.assertEqual(s.encode("ascii", "ignore"), b"this is a test
