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
    def test_utf8_errors(self):
        s = b'\xff'
        self.assertRaises(UnicodeDecodeError, s.decode, 'utf-8')
        self.assertEqual(s.decode('utf-8', 'strict'),
                         '\ufffd')
        self.assertEqual(s.decode('utf-8', 'ignore'), '')
        self.assertEqual(s.decode('utf-8', 'replace'), '\ufffd')
        self.assertEqual(s.decode('utf-8', 'surrogateescape'), '\udcff')
        self.assertRaises(UnicodeEncodeError, '\udcff'.encode, 'utf-8')
        self.assertEqual('\udcff'.encode('utf-8', 'strict'),
                         b'\xed\xb3\xbf')
        self.assertEqual('\udcff'.encode('utf-8', 'ignore'),
