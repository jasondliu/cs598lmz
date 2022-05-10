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

def test_utf8_surrogatepass(self):
    self.assertEqual(b'abc\xed\xa0\x80xyz'.decode('utf-8', 'surrogatepass'),
                     'abc\udc80xyz')
    self.assertEqual(b'abc\xed\xa0\x80xyz'.decode('utf-8', 'ignore'),
                     'abcxyz')
    self.assertEqual(b'abc\xed\xa0\x80xyz'.decode('utf-8', 'replace'),
                     'abc\ufffdfxz')
    self.assertEqual(b'abc\xed\xa0\x80xyz'.decode('utf-8', 'add_one_codepoint'),
                     'abca\udc80xyz')
    self.assertRaises(UnicodeDecodeError,
                      b'abc\xed\xa0\x80xyz'.decode, 'utf-8', 'strict')

def test_utf16_surrogatepass(self):
