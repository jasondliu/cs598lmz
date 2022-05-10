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

class TestDecodeErrorHandling(unittest.TestCase):

    def test_add_one_codepoint(self):
        self.assertEqual(b'\x80'.decode("ascii", "add_one_codepoint"),
                         u'\x80a')
        self.assertEqual(b'\xc2\x80'.decode("utf-8", "add_one_codepoint"),
                         u'\u0080a')
        self.assertEqual(b'\xe0\x80\x80'.decode("utf-8", "add_one_codepoint"),
                         u'\u0800a')
        self.assertEqual(b'\xf0\x80\x80\x80'.decode("utf-8", "add_one_codepoint"),
                         u'\U00010000a')
        self.assertEqual(b'\xf8\x80\x80\x80\x80'.decode("utf-8", "add_one_codepoint"),
                         u'
