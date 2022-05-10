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

class TestDecode(unittest.TestCase):

    def test_utf16_le_decode_error1(self):
        self.assertRaises(UnicodeDecodeError, '\xff\xfea'.decode, 'utf-16-le', 'strict')

    def test_utf16_le_decode_error2(self):
        self.assertEqual('\ufffd'.decode('utf-16-le', 'replace'), u'\ufffd')

    def test_utf16_le_decode_error3(self):
        self.assertEqual('\xff\xfea'.decode('utf-16-le', 'add_one_codepoint'), u'a')

    def test_utf16_le_decode_error4(self):
        self.assertRaises(UnicodeDecodeError, '\xff\xfea'.decode, 'utf-16-le', 'add_utf16_bytes')

    def test_utf16_le_decode_error5(self):
        self.assertE
