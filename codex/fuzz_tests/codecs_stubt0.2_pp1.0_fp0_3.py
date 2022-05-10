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
    def test_decode_error(self):
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii')
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii', 'strict')
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii', 'ignore')
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii', 'replace')
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii', 'backslashreplace')
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii', 'xmlcharrefreplace')
        self.assertRaises(UnicodeDecodeError, '\xff'.decode, 'ascii', 'add_one_codepoint')
        self.assertRaises(Un
