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

class Test_errors(unittest.TestCase):
    def test_strict_errors(self):
        self.assertRaises(UnicodeEncodeError, 'abc'.encode, 'utf-16', 'strict')
        self.assertRaises(UnicodeDecodeError, b'\xff'.decode, 'utf-16', 'strict')
        self.assertRaises(UnicodeEncodeError, '\U00010000'.encode, 'utf-16', 'strict')
        self.assertRaises(UnicodeDecodeError, b'\xff\xff'.decode, 'utf-32', 'strict')
        self.assertRaises(UnicodeDecodeError, b'\xff\xff\xff\xff\xff'.decode, 'utf-32', 'strict')

    def test_replace_errors(self):
        self.assertEqual('abc'.encode('utf-16', 'replace'), b'\xff\xfea\0b\0c\0')
        self.assertEqual(b'\xff
