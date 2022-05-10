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

class TestCodecs(unittest.TestCase):

    def test_utf_16_exception(self):
        s = b'\xff\xfe\x00\x61\x00\x62\x00\x63\x00\x00'
        for errors in "strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes":
            self.assertEqual(s.decode("utf-16", errors=errors),
                             "abc",
                             "utf-16 with errors=%s" % errors)
        for errors in "strict", "ignore", "replace", "add_one_codepoint", "add_utf32_bytes":
            self.assertEqual(s.decode("utf-32", errors=errors),
                             "abc",
                             "utf-32 with errors=%s" % errors)

    def test_utf16_decode(self):
        u = '\udc80'
        for errors in "strict", "ignore", "replace":
           
