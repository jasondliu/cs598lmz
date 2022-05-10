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
# Basic Unicode codec tests
#

class UnicodeCodecTest(unittest.TestCase):

    def setUp(self):
        # we want to make sure that errors are handled correctly,
        # we don't want error handlers to be triggered
        # when using the default ones.
        self.old_stderr = sys.stderr
        sys.stderr = StringIO()

    def tearDown(self):
        sys.stderr = self.old_stderr

    def test_utf8(self):
        # UTF-8
        for i in range(0x10000):
            b = chr(i).encode("utf-8")
            u = b.decode("utf-8")
            self.assertEqual(i, ord(u))
            b2 = u.encode("raw_unicode_escape")
            self.assertEqual(b, b2)

    def test_utf16(self):
        # UTF-16
        for i in range(0x10000):
            b = chr(i).en
