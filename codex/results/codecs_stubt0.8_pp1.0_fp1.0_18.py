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

class EncodingTest(unittest.TestCase):

    def test_utf8_error_handling(self):
        s = b"abc\xff"
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf8')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf_8')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf8','strict')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8','strict')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf_8', 'strict')
        self.assertEqual(s.decode('utf8', 'ignore'), 'abc')
        self.assertEqual(s.decode('utf-8', 'ignore'), 'abc')
        self.assertEqual(s.decode('
