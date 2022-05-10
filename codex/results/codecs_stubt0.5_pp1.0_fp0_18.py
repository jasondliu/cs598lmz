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

class Test_ErrorHandling(unittest.TestCase):

    def test_surrogates(self):
        self.assertRaises(UnicodeDecodeError, '\ud800'.decode, 'utf-8', 'strict')
        self.assertRaises(UnicodeEncodeError, '\ud800'.encode, 'utf-8', 'strict')

        self.assertEqual('\ud800'.decode('utf-8', 'ignore'), '')
        self.assertEqual('\ud800'.encode('utf-8', 'ignore'), b'')

        self.assertEqual('\ud800'.decode('utf-8', 'replace'), u'\ufffd')
        self.assertEqual('\ud800'.encode('utf-8', 'replace'), b'?')

        self.assertEqual('\ud800'.decode('utf-8', 'backslashreplace'), u'\\ud800')
        self.assertEqual('\ud800'.encode('utf-8', 'backslashreplace'), b'\\ud800
