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
        self.assertEqual(codecs.strict_errors, "strict")
        self.assertEqual(codecs.ignore_errors, "ignore")
        self.assertEqual(codecs.replace_errors, "replace")
        self.assertEqual(codecs.xmlcharrefreplace_errors, "xmlcharrefreplace")
        self.assertEqual(codecs.backslashreplace_errors, "backslashreplace")

        self.assertEqual(u"abc".encode("ascii", "add_one_codepoint"), "aabc")
        self.assertEqual(u"abc".encode("utf-16", "add_utf16_bytes"), b'\xff\xfe\x61\x00\x61\x00\x62\x00\x63\x00')
        self.assertEqual(u"abc".encode("utf-32", "add_utf32_bytes"), b'
