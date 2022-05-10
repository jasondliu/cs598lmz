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

class TestUTF8(unittest.TestCase):
    # TODO: use a context manager, as soon as we get Python 2.7 support
    def setUp(self):
        self.old_environ = os.environ
        os.environ = dict(self.old_environ)
        os.environ["PYTHONUTF8"] = "1"

    def tearDown(self):
        os.environ = self.old_environ

    def test_utf8_errors(self):
        # Issue #1727: UTF-8 unicode error handler incorrectly applied
        # to non-UTF-8 encoded data
        data = b"abc\xff"
        self.assertRaises(UnicodeDecodeError, data.decode, "utf-8", "strict")
        self.assertEqual(data.decode("utf-8", "add_one_codepoint"), "\uFFFDb\uFFFDc\uFFFDF")

    def test_utf8_encoding(self):
        # Issue #1727: UTF-
