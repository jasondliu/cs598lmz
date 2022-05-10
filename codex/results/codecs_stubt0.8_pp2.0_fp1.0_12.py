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

class StrTest(unittest.TestCase):

    def test_latin1(self):
        # encoding to latin-1
        self.assertEqual(b'hello', 'hello'.encode('latin-1'))
        self.assertEqual(b'\xe9', '\xe9'.encode('latin-1'))
        self.assertRaises(UnicodeEncodeError, '\u2020'.encode, 'latin-1')
        self.assertRaises(UnicodeEncodeError, '\xff'.encode, 'latin-1',
                          'replace')
        self.assertEqual(b'?', '\u2020'.encode('latin-1', 'replace'))

        # decoding from latin-1
        self.assertEqual('hello', b'hello'.decode('latin-1'))
        self.assertEqual('\xe9', b'\xe9'.decode('latin-1'))
        self.assertRaises(UnicodeDecodeError, b'\xff'.
