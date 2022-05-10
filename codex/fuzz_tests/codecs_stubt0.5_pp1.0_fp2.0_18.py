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

class UnicodeErrorTestCase(unittest.TestCase):
    def test_unicode_decode(self):
        # 'ascii' codec with non-ASCII input
        self.assertRaises(UnicodeError, '\xff'.decode, 'ascii')
        self.assertRaises(UnicodeError, '\xff'.decode, 'ascii', 'strict')
        self.assertEqual('\xff'.decode('ascii', 'ignore'), '')
        self.assertEqual('\xff'.decode('ascii', 'replace'), '?')
        self.assertEqual('\xff'.decode('ascii', 'backslashreplace'), '\\xff')
        self.assertEqual('\xff'.decode('ascii', 'xmlcharrefreplace'), '&#255;')
        self.assertEqual('\xff'.decode('ascii', 'add_one_codepoint'), 'a\ufffd')

        # 'ascii' codec with non-ASCII input and a UnicodeDecode
