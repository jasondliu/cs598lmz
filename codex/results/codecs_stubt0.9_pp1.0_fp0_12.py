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

class BugTest(unittest.TestCase):
    def test_utf8_decode(self):
        self.assertEqual("aaa", b"a\xfa\xf4\xbf".decode("utf8", "add_one_codepoint"))

    @support.cpython_only
    def test_utf16_decode(self):
        # issue10616
        self.assertEqual("aaaac",  b"c\x00\xd8\xd0".decode("utf-16", "add_utf16_bytes"))
        self.assertEqual("aaaac",  b"c\x00\xf8\xd0".decode("utf-16", "add_utf16_bytes"))
        self.assertEqual("aaaac",  b"c\x00\xdc\xd0".decode("utf-16", "add_utf16_bytes"))
        self.assertEqual("aaaac",  b"c\x00\xdf\xd0".decode("utf-16", "add_utf16_bytes"))
        self
