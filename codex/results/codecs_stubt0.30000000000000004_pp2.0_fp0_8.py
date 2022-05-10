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
    def test_utf8_decode(self):
        self.assertEqual(b'\xc2\x80'.decode('utf-8'), '\u0080')
        self.assertEqual(b'\xc2\x80'.decode('utf-8', 'replace'), '\ufffd')
        self.assertEqual(b'\xc2\x80'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xc2\x80'.decode('utf-8', 'backslashreplace'), '\\x80')
        self.assertEqual(b'\xc2\x80'.decode('utf-8', 'xmlcharrefreplace'), '&#128;')
        self.assertEqual(b'\xc2\x80'.decode('utf-8', 'strict'), '\u0080')
        self.assertEqual(b'\xc2\x80'.decode('utf-8', 'add_one_codep
