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

    def test_decode_error_handling(self):
        # Test that the codecs module's error handling works
        # with UTF-8 as well.
        self.assertEqual(b'\xff'.decode("utf-8", "strict"),
                         u'\ufffd')
        self.assertEqual(b'\xff'.decode("utf-8", "ignore"),
                         u'')
        self.assertEqual(b'\xff'.decode("utf-8", "replace"),
                         u'\ufffd')

        self.assertEqual(b'\xff\xff'.decode("utf-8", "strict"),
                         u'\ufffd\ufffd')
        self.assertEqual(b'\xff\xff'.decode("utf-8", "ignore"),
                         u'')
        self.assertEqual(b'\xff\xff'.decode("utf-8", "replace"),
                         u'\ufffd\ufffd')

        self.assertEqual(
