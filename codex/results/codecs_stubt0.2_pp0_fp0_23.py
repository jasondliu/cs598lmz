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
    def test_encode(self):
        self.assertEqual(b'abc', 'abc'.encode('ascii'))
        self.assertEqual(b'abc', 'abc'.encode('latin-1'))
        self.assertEqual(b'abc', 'abc'.encode('utf-8'))
        self.assertEqual(b'abc', 'abc'.encode('utf-16'))
        self.assertEqual(b'abc', 'abc'.encode('utf-32'))

        self.assertEqual(b'\xe4\xb8\x96', '\u4e16'.encode('utf-8'))
        self.assertEqual(b'\xff\xfe\x16\x4e', '\u4e16'.encode('utf-16'))
        self.assertEqual(b'\xff\xfe\x00\x00\x16\x4e\x00\x00', '\u4e16
