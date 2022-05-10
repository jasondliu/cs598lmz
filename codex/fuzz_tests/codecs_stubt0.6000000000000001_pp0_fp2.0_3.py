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

class TestEscapeDecode(unittest.TestCase):
    def test_xmlcharrefreplace(self):
        self.assertEqual("&#65533;", "\ufffd".encode("ascii", "xmlcharrefreplace").decode("ascii"))
        self.assertEqual("&#65533;", "\ufffd".encode("ascii", "xmlcharrefreplace").decode("ascii"))
        self.assertEqual("&#65533;", "\ud800".encode("ascii", "xmlcharrefreplace").decode("ascii"))
        self.assertEqual("abc&#65533;&#65533;", "abc\ud800\udc00".encode("ascii", "xmlcharrefreplace").decode("ascii"))
        self.assertEqual("&#65533;", "\udc00".encode("ascii", "xmlcharrefreplace").decode("ascii"))
        self.assertEqual("&#65533;", "\udbff".encode("asci
