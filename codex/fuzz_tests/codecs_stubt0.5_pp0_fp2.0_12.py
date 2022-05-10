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
    def test_utf8(self):
        self.assertEqual('\U00012345'.encode('utf-8'), b'\xf0\x92\x8d\x85')
        self.assertEqual(b'\xf0\x92\x8d\x85'.decode('utf-8'), '\U00012345')

    def test_utf8_errors(self):
        self.assertEqual(b'\xff'.decode('utf-8', 'replace'), '\ufffd')
        self.assertEqual(b'\xff'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xff'.decode('utf-8', 'backslashreplace'), '\\xff')
        self.assertEqual(b'\xff'.decode('utf-8', 'xmlcharrefreplace'), '&#255;')
        self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'utf-8', '
