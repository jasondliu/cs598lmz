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

    def test_all(self):
        self.assertIs(codecs.lookup("iso8859-1"),
                      codecs.lookup("latin-1"))
        self.assertIs(codecs.lookup("iso8859_1"),
                      codecs.lookup("latin_1"))
        self.assertIs(codecs.lookup("8859-1"),
                      codecs.lookup("latin-1"))
        self.assertIs(codecs.lookup("8859_1"),
                      codecs.lookup("latin_1"))
        self.assertIs(codecs.lookup("cp819"),
                      codecs.lookup("iso8859-1"))
        self.assertIs(codecs.lookup("latin-1"),
                      codecs.lookup("cp1252"))

        s = u"δοκιμή"
        self.assertEqual(codecs.utf_8_encode(s)[0],
