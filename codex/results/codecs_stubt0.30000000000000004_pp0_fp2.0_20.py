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

#
#   Encoding tests
#

class Test_UTF8(unittest.TestCase):

    def test_utf8_encode(self):
        self.assertEqual(b'\xc3\xa9\xc3\xa9\xc3\xa9\xc3\xa9',
                         'éééé'.encode('utf-8'))
        self.assertEqual(b'\xe2\x82\xac\xe2\x82\xac\xe2\x82\xac\xe2\x82\xac',
                         '€€€€'.encode('utf-8'))
        self.assertEqual(b'\xf0\x90\x80\x80\xf0\x90\x80\x80\xf0\x90\x80\x80\xf0\x90\x80\x80',
                         '𐀀𐀀𐀀𐀀'.encode('utf-8'))
        self.assertEqual(b'\xf4\x
