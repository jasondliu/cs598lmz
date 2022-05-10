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

class TestCase(unittest.TestCase):
    def test_utf_16_be_decode(self):
        self.assertEqual(b'\x00\x61'.decode('utf-16-be', 'add_one_codepoint'), 'a')
        self.assertEqual(b'\x00\x61'.decode('utf-16-be', 'add_utf16_bytes'), 'a')
        self.assertEqual(b'\x00\x61'.decode('utf-16-be', 'add_utf32_bytes'), 'a')

    def test_utf_16_le_decode(self):
        self.assertEqual(b'\x61\x00'.decode('utf-16-le', 'add_one_codepoint'), 'a')
        self.assertEqual(b'\x61\x00'.decode('utf-16-le', 'add_utf16_bytes'), 'a')
        self.assertEqual(b'\x61\x00'.decode('utf-16
