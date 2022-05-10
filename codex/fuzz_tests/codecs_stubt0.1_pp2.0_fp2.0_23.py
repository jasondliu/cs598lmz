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
    def test_decode_error(self):
        self.assertEqual(b'\xff'.decode('ascii', 'strict'), '\ufffd')
        self.assertEqual(b'\xff'.decode('ascii', 'ignore'), '')
        self.assertEqual(b'\xff'.decode('ascii', 'replace'), '?')
        self.assertEqual(b'\xff'.decode('ascii', 'add_one_codepoint'), 'a')
        self.assertEqual(b'\xff'.decode('ascii', 'add_utf16_bytes'), 'ab')
        self.assertEqual(b'\xff'.decode('ascii', 'add_utf32_bytes'), 'abcd')

        self.assertEqual(b'\xff'.decode('utf-8', 'strict'), '\ufffd')
        self.assertEqual(b'\xff'.decode('utf-8', 'ignore'), '')
