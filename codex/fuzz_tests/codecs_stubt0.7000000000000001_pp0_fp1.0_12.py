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

class UnicodeDecodeErrorTest(unittest.TestCase):
    def test_lone_surrogate(self):
        self.assertEqual(b'\xED\xA0\x80'.decode('utf-8', 'surrogatepass'),
                         '\U000dc080')
        self.assertEqual(b'\xED\xA0\x80'.decode('utf-8', 'replace'),
                         '\ufffd\ufffd\ufffd')
        self.assertEqual(b'\xED\xA0\x80'.decode('utf-8', 'ignore'),
                         '')
        self.assertRaises(UnicodeDecodeError,
                          b'\xED\xA0\x80'.decode, 'utf-8', 'strict')
        self.assertRaises(UnicodeDecodeError,
                          b'\xED\xA0\x80'.decode, 'utf-8', 'backslashreplace')
        self.assertEqual(b'\xED\x
