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

class TestUnicodeErrors(unittest.TestCase):
    def test_register(self):
        # Registering errors tests
        self.assertRaises(TypeError, codecs.register_error, -1)
        self.assertRaises(TypeError, codecs.register_error, "add_one_codepoint", 0)

    def test_lookup(self):
        # Looking up errors tests
        with test.support.check_py3k_warnings():
            self.assertEqual(codecs.lookup_error("strict"), (None, None))
        self.assertEqual(codecs.lookup_error("add_one_codepoint"),
                         (add_one_codepoint, None))
        self.assertRaises(LookupError, codecs.lookup_error, "bogus_error")

    def test_add_one_codepoint(self):
        # Test adding one codepoint
        sb = "ab\u20ac".encode("ISO-8859-15")
        se
