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
        # Test UTF-8 decoding
        self.assertEqual(b'\xc3\xa4'.decode('utf-8'), '\xe4')
        self.assertEqual(b'\xc3\xa4\xe2\x82\xac'.decode('utf-8'), '\xe4\u20ac')
        self.assertEqual(b'\xc3\xa4\xe2\x82'.decode('utf-8', 'ignore'), '\xe4')
        self.assertEqual(b'\xc3\xa4\xe2\x82'.decode('utf-8', 'replace'), '\xe4\ufffd')
        self.assertEqual(b'\xc3\xa4\xe2\x82'.decode('utf-8', 'backslashreplace'), '\\xe4\\uFFFD')
        self.assertEqual(b'\xc3\xa4\xe2\x82'.decode
