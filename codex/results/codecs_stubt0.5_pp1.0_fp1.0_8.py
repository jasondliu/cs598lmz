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

class TestErrorHandling(unittest.TestCase):
    def test_surrogatepass(self):
        self.assertRaises(UnicodeDecodeError,
                          '\udc80'.encode, 'utf-8', 'surrogatepass')
        self.assertEqual('\udc80'.encode('utf-8', 'surrogatepass'),
                         '\udc80'.encode('utf-8', 'replace'))

    def test_surrogateescape(self):
        self.assertEqual('\udc80'.encode('utf-8', 'surrogateescape'), b'\x80')
        self.assertEqual(b'\x80'.decode('utf-8', 'surrogateescape'), '\udc80')

    def test_surrogateescape_lone_surrogate(self):
        self.assertEqual(b'\xed\xb0\x80'.decode('utf-8', 'surrogateescape'),
                         '\udc80')
        self.assertEqual(
