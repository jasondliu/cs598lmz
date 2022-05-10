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
        # Test UTF-8
        self.assertEqual(u'\u20ac'.encode('utf-8'), b'\xe2\x82\xac')
        self.assertEqual('\xe2\x82\xac'.decode('utf-8'), u'\u20ac')
        self.assertEqual(u'\u20ac'.encode('utf-8-sig'), b'\xef\xbb\xbf\xe2\x82\xac')
        self.assertEqual('\xef\xbb\xbf\xe2\x82\xac'.decode('utf-8-sig'), u'\u20ac')
        self.assertEqual(u'\u20ac'.encode('utf-8-sig'), b'\xef\xbb\xbf\xe2\x82\xac')
        self.assertEqual('\xef\xbb\xbf\xe2\x
