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
    def test_utf8_decode(self):
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'add_one_codepoint'), '\xc3\xa4a')
        self.assertEqual(b'\xe2\x82\xac'.decode('utf-8', 'add_one_codepoint'), '\xe2\x82\xaca')
        self.assertEqual(b'\xf0\x90\x8c\xbc'.decode('utf-8', 'add_one_codepoint'), '\xf0\x90\x8c\xbca')

    def test_utf8_encode(self):
        self.assertEqual('\xc3\xa4'.encode('utf-8', 'add_utf16_bytes'), b'\xc3\xa4ab')
        self.assertEqual('\xe2\x82\xac'.encode('utf-8', 'add_utf16_
