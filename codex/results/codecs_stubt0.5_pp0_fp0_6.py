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

class TestUTF8(unittest.TestCase):
    def test_utf8_decode_error(self):
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'utf-8')

    def test_utf8_decode_replace(self):
        self.assertEqual('\ufffd'.decode('utf-8', 'replace'), '?')

    def test_utf8_decode_ignore(self):
        self.assertEqual('\xff'.decode('utf-8', 'ignore'), '')

    def test_utf8_decode_xmlcharrefreplace(self):
        self.assertEqual('\xff'.decode('utf-8', 'xmlcharrefreplace'), '&#255;')

    def test_utf8_decode_backslashreplace(self):
        self.assertEqual('\xff'.decode('utf-8', 'backslashreplace'), '\\xff')

    def test_utf8_decode_add_one_codepoint(self):
        self.assertE
