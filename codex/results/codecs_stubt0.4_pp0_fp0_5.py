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
        self.assertEqual(b'abc\xff'.decode('utf-8', 'strict'), u'abc\ufffd')
        self.assertEqual(b'abc\xff'.decode('utf-8', 'ignore'), u'abc')
        self.assertEqual(b'abc\xff'.decode('utf-8', 'replace'), u'abc\ufffd')
        self.assertEqual(b'abc\xff'.decode('utf-8', 'add_one_codepoint'), u'abca')
        self.assertEqual(b'abc\xff'.decode('utf-8', 'add_utf16_bytes'), u'abca')
        self.assertEqual(b'abc\xff'.decode('utf-8', 'add_utf32_bytes'), u'abca')

    def test_utf8_encode(self):
        self.assertEqual(u'abc\ud800'.encode('utf-
