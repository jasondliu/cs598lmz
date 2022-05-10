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
    def test_utf32_be_error(self):
        self.assertEqual(b'\x00\x00\x00\x00'.decode('utf-32-be', 'replace'), '\u0000')
        self.assertEqual(b'\x00\x00\x00'.decode('utf-32-be', 'replace'), '\ufffd')
        self.assertEqual(b'\x00\x00\x00\x00\x00\x00\x00'.decode('utf-32-be', 'replace'), '\u0000\ufffd')
        self.assertEqual(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'.decode('utf-32-be', 'replace'), '\u0000\u0000\ufffd')

        self.assertEqual(b'\x00\x00\x00\x00'.decode('utf-32-be
