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

class CodecsTests(unittest.TestCase):

    def test_register_error(self):
        s = "abc"
        self.assertEqual(codecs.escape_encode(s)[0], b'abc')
        self.assertEqual(codecs.escape_encode(s, errors="add_one_codepoint")[0], b'aabc')
        self.assertEqual(codecs.escape_encode(s, errors="add_utf16_bytes")[0], b'ababc')
        self.assertEqual(codecs.escape_encode(s, errors="add_utf32_bytes")[0], b'abcdabc')

    def test_decode_error(self):
        self.assertEqual(b'test'.decode('ascii', 'strict'), "test")
        self.assertRaises(UnicodeDecodeError, b'test'.decode, 'ascii', 'strict', 0)
        self.assertRaises(UnicodeDecodeError, b
