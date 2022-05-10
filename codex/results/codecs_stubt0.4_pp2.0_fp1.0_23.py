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

class Test_UTF16(unittest.TestCase):
    def test_utf16_le(self):
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62\x00\x63',
                         b'abc'.decode('utf-16-le', 'add_one_codepoint'))
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62\x00\x63',
                         b'abc'.decode('utf-16-le', 'add_utf16_bytes'))
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62\x00\x63',
                         b'abc'.decode('utf-16-le', 'add_utf32_bytes'))

    def test_utf16_be(self):
        self.assertEqual(b'\xfe\xff\x61\x00\x62\x00\x63\x00',
                         b'abc'.dec
