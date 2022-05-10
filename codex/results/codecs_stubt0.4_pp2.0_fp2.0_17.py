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
    def test_utf16_le(self):
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62'.decode('utf-16-le'), 'ab')
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62'.decode('utf-16-le', 'strict'), 'ab')
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62'.decode('utf-16-le', 'ignore'), '')
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62'.decode('utf-16-le', 'replace'), 'ab')
        self.assertEqual(b'\xff\xfe\x00\x61\x00\x62'.decode('utf-16-le', 'add_one_codepoint'), 'aab')
        self.assertEqual(b'
