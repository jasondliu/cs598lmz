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

    def test_register(self):
        self.assertEqual(codecs.lookup_error("add_one_codepoint"),
                         (add_one_codepoint, None, None))
        self.assertEqual(codecs.lookup_error("add_utf16_bytes"),
                         (add_utf16_bytes, None, None))
        self.assertEqual(codecs.lookup_error("add_utf32_bytes"),
                         (add_utf32_bytes, None, None))

    def test_strict(self):
        self.assertEqual("abc".encode("ascii", "strict"), b"abc")
        self.assertRaises(UnicodeError, "abc\u1234".encode, "ascii", "strict")

    def test_ignore(self):
        self.assertEqual("abc".encode("ascii", "ignore"), b"abc")
        self.assertEqual("abc\u1234".en
