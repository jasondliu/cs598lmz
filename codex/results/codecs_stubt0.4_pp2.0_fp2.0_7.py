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

class TestUnicodeDecodeError(unittest.TestCase):
    def test_add_one_codepoint(self):
        s = b'\x80'
        self.assertRaises(UnicodeDecodeError, s.decode, 'ascii', 'add_one_codepoint')
        self.assertEqual(s.decode('ascii', 'ignore'), '')
        self.assertEqual(s.decode('ascii', 'replace'), '?')
        self.assertEqual(s.decode('ascii', 'backslashreplace'), '\\x80')
        self.assertEqual(s.decode('ascii', 'xmlcharrefreplace'), '&#128;')
        self.assertEqual(s.decode('ascii', 'add_one_codepoint'), 'a')

    def test_add_utf16_bytes(self):
        s = b'\x80'
        self.assertRaises(UnicodeDecodeError, s.decode, 'asci
