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
        self.assertEqual(codecs.strict_errors, None)
        self.assertEqual(codecs.replace_errors, None)
        self.assertEqual(codecs.ignore_errors, None)
        self.assertEqual(codecs.lookup_error("strict"), None)
        self.assertEqual(codecs.lookup_error("replace"), None)
        self.assertEqual(codecs.lookup_error("ignore"), None)
        self.assertEqual(codecs.lookup_error("backslashreplace"), None)
        self.assertEqual(codecs.lookup_error("xmlcharrefreplace"), None)
        self.assertEqual(codecs.lookup_error("namereplace"), None)
        self.assertEqual(codecs.lookup_error("add_one_codepoint"), add_one_codepoint)
        self.assertEqual
