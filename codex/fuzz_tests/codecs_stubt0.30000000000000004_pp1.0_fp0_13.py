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

class Test_utf_16_be_decode(unittest.TestCase):

    def test_decode_error_handling(self):
        self.assertEqual(codecs.utf_16_be_decode(b'abcd', "strict", True),
                         (u'\udc00', 2))
        self.assertEqual(codecs.utf_16_be_decode(b'abcd', "strict", False),
                         (u'\udc00', 2))
        self.assertEqual(codecs.utf_16_be_decode(b'abcd', "ignore", True),
                         (u'', 2))
        self.assertEqual(codecs.utf_16_be_decode(b'abcd', "ignore", False),
                         (u'', 2))
        self.assertEqual(codecs.utf_16_be_decode(b'abcd', "replace", True),
                         (u'\ufffd\ufffd', 2))
        self.assertEqual(
