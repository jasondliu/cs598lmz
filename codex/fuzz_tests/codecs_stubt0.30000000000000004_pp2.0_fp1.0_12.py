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

class TestDecode(unittest.TestCase):

    def test_utf8(self):
        self.assertEqual(u'\u20ac'.encode('utf-8'), b'\xe2\x82\xac')
        self.assertEqual(u'\u20ac'.encode('utf-8', 'strict'), b'\xe2\x82\xac')
        self.assertEqual(u'\u20ac'.encode('utf-8', 'replace'), b'\xe2\x82\xac')
        self.assertEqual(u'\u20ac'.encode('utf-8', 'ignore'), b'')
        self.assertEqual(u'\u20ac'.encode('utf-8', 'xmlcharrefreplace'), b'&#8364;')
        self.assertEqual(u'\u20ac'.encode('utf-8', 'backslashreplace'), b'\\u20ac')
        self.assertEqual(u'\u20ac'.encode('utf-8', '
