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

class Test_codecs(unittest.TestCase):
    def test_utf8_errors(self):
        self.assertEqual(b'abc\x80def'.decode('utf-8', 'strict'),
                         u'abc\udc80def')
        self.assertEqual(b'abc\x80def'.decode('utf-8', 'replace'),
                         u'abc\ufffddef')
        self.assertEqual(b'abc\x80def'.decode('utf-8', 'ignore'),
                         u'abcdef')
        self.assertEqual(b'abc\x80\x80def'.decode('utf-8', 'ignore'),
                         u'abcdef')
        self.assertEqual(b'abc\xc0\x80def'.decode('utf-8', 'ignore'),
                         u'abcdef')
        self.assertEqual(b'abc\x80def'.decode('utf-8', 'backslashreplace'),
                         u'abc\\x80def')
        self.assertEqual(b
