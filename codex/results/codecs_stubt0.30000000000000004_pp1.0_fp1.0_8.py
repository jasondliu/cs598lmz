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
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8'), '\xe9\n')
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8', 'strict'), '\xe9\n')
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8', 'ignore'), '\n')
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8', 'replace'), '\xe9\ufffd')
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8', 'add_one_codepoint'), '\xe9a\n')
        self.assertEqual(b'\xc3\xa9\n'.decode('utf-8', 'add_utf16_bytes'), '\xe
