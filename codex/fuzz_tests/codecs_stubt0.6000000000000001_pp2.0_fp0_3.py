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

class CodecsTest(unittest.TestCase):
    def test_decode_error(self):
        self.assertEqual('abc'.encode('ascii', 'strict'), b'abc')
        self.assertEqual(b'abc'.decode('ascii', 'strict'), 'abc')

        self.assertRaises(UnicodeDecodeError,
                          b'\xff'.decode, 'ascii', 'strict')
        self.assertRaises(UnicodeDecodeError,
                          b'\xff'.decode, 'ascii', 'replace')
        self.assertEqual(b'\xff'.decode('ascii', 'ignore'), '')
        self.assertEqual(b'\xff'.decode('ascii', 'backslashreplace'), '\\xff')

        self.assertEqual(b'\xff'.decode('ascii', 'add_one_codepoint'), '\ufffd')
        self.assertEqual(b'\xff'.decode('utf16', '
