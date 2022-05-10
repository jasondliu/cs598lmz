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

class Test_UTF8(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc',
                         codecs.utf_8_encode('\xe4\xf6\xfc')[0])
        self.assertEqual(b'\xe4\xbd\xa0\xe5\xa5\xbd',
                         codecs.utf_8_encode('\u4f60\u597d')[0])
        self.assertEqual(b'\xf0\xa4\xad\xa2',
                         codecs.utf_8_encode('\U00024b62')[0])

        self.assertRaises(UnicodeEncodeError, codecs.utf_8_encode, "\ud800")

        self.assertEqual(b'\xc3\xa4\xc3\xb6\xc3\xbc',
                         codecs.utf_8_encode('\xe4\xf6\
