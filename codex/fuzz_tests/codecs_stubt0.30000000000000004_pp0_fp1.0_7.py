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
        self.assertEqual(b'abc'.decode('utf-8'), 'abc')
        self.assertEqual(b'\xc3\xbc'.decode('utf-8'), '\xfc')
        self.assertEqual(b'\xe2\x82\xac'.decode('utf-8'), '\u20ac')
        self.assertEqual(b'\xe2\x82'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xe2\x82'.decode('utf-8', 'replace'), '\ufffd')
        self.assertEqual(b'\xe2\x82'.decode('utf-8', 'add_one_codepoint'), 'a')
        self.assertEqual(b'\xe2\x82'.decode('utf-8', 'add_utf16_bytes'), '\udc00')
        self.assertEqual(
