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
        self.assertEqual(
            codecs.register_error("strict", None),
            codecs.strict_errors
        )
        self.assertEqual(
            codecs.register_error("ignore", None),
            codecs.ignore_errors
        )
        self.assertEqual(
            codecs.register_error("replace", None),
            codecs.replace_errors
        )
        self.assertEqual(
            codecs.register_error("xmlcharrefreplace", None),
            codecs.xmlcharrefreplace_errors
        )
        self.assertEqual(
            codecs.register_error("backslashreplace", None),
            codecs.backslashreplace_errors
        )
        self.assertEqual(
            codecs.register_error("namereplace", None),
            codecs.namereplace_errors
        )

    def test_lookup_error(self):
        self.assertEqual(

