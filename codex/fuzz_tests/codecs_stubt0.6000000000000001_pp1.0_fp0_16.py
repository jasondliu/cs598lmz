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

class TestUTF16(unittest.TestCase):
    def test_utf16(self):
        # UTF-16 with BOM
        text = '\u20ac'
        self.assertEqual(text.encode('utf-16'), b'\xff\xfe\xac\x20')
        self.assertEqual(text.encode('utf-16-le'), b'\xac\x20')
        self.assertEqual(text.encode('utf-16-be'), b'\xac\x20')

    def test_utf16_errors(self):
        # UTF-16 with BOM
        text = '\u20ac'
        #  this is a utf-16-le encoded euro symbol, but with the
        #  last two bytes missing.
        self.assertRaises(UnicodeDecodeError, b'\xac\x20'.decode, 'utf-16')
        self.assertRaises(UnicodeDecodeError, b'\xac\x20'.decode, 'utf-16-le
