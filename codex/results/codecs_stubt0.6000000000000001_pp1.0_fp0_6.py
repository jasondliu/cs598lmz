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

class TestUnicode(unittest.TestCase):

    def test_ascii(self):
        u = chr(0x7F)
        self.assertEqual(u.encode('ascii'), b'\x7f')
        u = chr(0x80)
        self.assertRaises(UnicodeEncodeError,
                          u.encode, 'ascii')
        u = chr(0xFF)
        self.assertRaises(UnicodeEncodeError,
                          u.encode, 'ascii')
        self.assertEqual(u.encode('ascii', 'ignore'), b'')
        self.assertEqual(u.encode('ascii', 'replace'), b'?')
        self.assertEqual(u.encode('ascii', 'backslashreplace'), b'\\xff')
        self.assertEqual(u.encode('ascii', 'xmlcharrefreplace'),
                         b'&#255;')
        self.assertEqual(
