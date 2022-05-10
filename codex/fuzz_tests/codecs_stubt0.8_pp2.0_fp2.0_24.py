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

class ErrorHandlerTest(unittest.TestCase):
    def test_errorhandler_lookup(self):
        self.assertIs(codecs.lookup_error("strict"), codecs.strict_errors)
        self.assertIs(codecs.lookup_error("ignore"), codecs.ignore_errors)
        self.assertIs(codecs.lookup_error("replace"), codecs.replace_errors)
        self.assertIs(codecs.lookup_error("add_one_codepoint"), add_one_codepoint)
        self.assertIs(codecs.lookup_error("add_utf16_bytes"), add_utf16_bytes)
        self.assertIs(codecs.lookup_error("add_utf32_bytes"), add_utf32_bytes)

    def test_strict(self):
        for encoding in ('utf_7', 'utf_16', 'utf_32'):
            with self.assertRaises(UnicodeEncodeError) as cm:
                codecs.encode(b
