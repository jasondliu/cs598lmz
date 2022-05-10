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

class UnicodeDecodeErrorTest(unittest.TestCase):

    def test_bad_decode_replace(self):
        # Test bad decode with 'replace' error handler
        u = "\u3042\ufffd"
        b = b"\xe3\x81\x82\xef\xbf\xbd"
        self.assertEqual(u, b.decode("utf-8", "replace"))
        self.assertEqual(u, b.decode("utf-8", "ignore"))
        self.assertEqual(u, b.decode("utf-8", "backslashreplace"))
        self.assertEqual(u, b.decode("utf-8", "xmlcharrefreplace"))
        self.assertEqual(u, b.decode("utf-8", "strict"))

    def test_bad_decode_ignore(self):
        # Test bad decode with 'ignore' error handler
        u = "\u3042"
        b = b"\xe3\x81\x82\xef\xbf\xbd
