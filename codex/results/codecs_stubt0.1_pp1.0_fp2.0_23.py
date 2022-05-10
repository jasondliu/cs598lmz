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
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'strict'), '\u00e4')
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'replace'), '\u00e4')
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'ignore'), '')
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'add_one_codepoint'), '\u00e4a')
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'add_utf16_bytes'), '\u00e4ab')
        self.assertEqual(b'\xc3\xa4'.decode('utf-8', 'add_utf32_bytes'), '\u00e4abcd')

        self.assertEqual(
