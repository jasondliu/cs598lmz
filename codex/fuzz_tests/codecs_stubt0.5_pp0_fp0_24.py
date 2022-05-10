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
        # Test UTF-8 coding
        self.assertEqual(b'\xc3\xa9\xc3\xa0\xc3\xa7\xc3\xa8'.decode('utf-8'),
                         '\xe9\xe0\xe7\xe8')
        self.assertEqual('\xe9\xe0\xe7\xe8'.encode('utf-8'),
                         b'\xc3\xa9\xc3\xa0\xc3\xa7\xc3\xa8')
        self.assertEqual(b'\xc3\xa9\xc3\xa0\xc3\xa7\xc3\xa8'.decode('utf-8'),
                         '\u00e9\u00e0\u00e7\u00e8')
        self.assertEqual('\u00e9\u00e0\u00e7\u00e8'.encode('utf-8'),
                         b'\xc
