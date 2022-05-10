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

class UnicodeTest(unittest.TestCase):
    def test_latin1(self):
        s = '€\u20ac'
        self.assertEqual(s.encode('latin-1'), b'\x80\xe2\x82\xac')
        self.assertEqual(s.encode('latin-1', 'add_one_codepoint'), b'a\x80\xe2\x82\xac')
        self.assertEqual(s.encode('latin-1', 'add_utf16_bytes'), b'ab\x80\xe2\x82\xac')
        self.assertEqual(s.encode('latin-1', 'add_utf32_bytes'), b'abcd\x80\xe2\x82\xac')

    def test_latin1_replace(self):
        s = '\u0100\u20ac'
        self.assertEqual(s.encode('latin-1', 'replace'), b'??\xe2\x82\xac
