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
        self.assertEqual(codecs.lookup_error("add_one_codepoint"),
                         add_one_codepoint)
        self.assertEqual(codecs.lookup_error("add_utf16_bytes"),
                         add_utf16_bytes)
        self.assertEqual(codecs.lookup_error("add_utf32_bytes"),
                         add_utf32_bytes)

    def test_lookup_error(self):
        self.assertEqual(codecs.lookup_error("strict"),
                         codecs.strict_errors)
        self.assertEqual(codecs.lookup_error("ignore"),
                         codecs.ignore_errors)
        self.assertEqual(codecs.lookup_error("replace"),
                         codecs.replace_errors)
        self.assertEqual(codecs.lookup_error("backslashreplace"),
                         codecs.backslash
