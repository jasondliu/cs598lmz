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
    def test_decode_error_add_one_codepoint(self):
        s = '\x80'.encode('latin1')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8', 'strict')
        self.assertEqual(s.decode('utf-8', 'replace'), '\ufffd')
        self.assertEqual(s.decode('utf-8', 'ignore'), '')
        self.assertEqual(s.decode('utf-8', 'add_one_codepoint'), 'a')

    def test_decode_error_add_utf16_bytes(self):
        s = '\x80'.encode('latin1')
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-16', 'strict')
        self.assertEqual(s.decode('utf-16', 'replace'), '\ufffd')
        self.assertEqual(s.dec
