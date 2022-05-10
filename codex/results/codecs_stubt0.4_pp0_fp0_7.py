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

class CodecsModuleTest(unittest.TestCase):
    def test_encode_decode_error(self):
        # Testing the 'strict' error handler
        self.assertRaises(UnicodeEncodeError, 'abc'.encode, 'ascii', 'strict')
        self.assertRaises(UnicodeDecodeError, b'abc'.decode, 'ascii', 'strict')

        # Testing the 'replace' error handler
        self.assertEqual('abc'.encode('ascii', 'replace'), b'abc')
        self.assertEqual(b'abc'.decode('ascii', 'replace'), 'abc')

        # Testing the 'ignore' error handler
        self.assertEqual('abc'.encode('ascii', 'ignore'), b'')
        self.assertEqual(b'abc'.decode('ascii', 'ignore'), '')

        # Testing the 'xmlcharrefreplace' error handler
        self.assertEqual('\u20ac'.encode('ascii', 'xmlcharref
