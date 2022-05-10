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
        self.assertEqual(b'\xff\xfea\x00'.decode('utf-16'), 'a')
        self.assertEqual(b'\xff\xfea\x00b\x00'.decode('utf-16'), 'ab')
        self.assertEqual(b'\xff\xfea\x00b\x00c\x00'.decode('utf-16'), 'abc')
        self.assertEqual(b'\xff\xfea\x00b\x00c\x00d\x00'.decode('utf-16'), 'abcd')
        self.assertEqual(b'\xff\xfea\x00b\x00c\x00d\x00e\x00'.decode('utf-16'), 'abcde')
        self.assertEqual(b'\xff\xfea\x00b\x00c\x00d\x00e\x00f\x00
