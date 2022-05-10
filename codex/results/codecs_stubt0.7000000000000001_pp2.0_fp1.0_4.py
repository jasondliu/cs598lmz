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
    def test_readbuffer_encode(self):
        expect = "abcdefghij"
        self.assertEqual(list(codecs.iterdecode(expect, "utf-8")),
                         list(codecs.iterdecode(io.BytesIO(expect), "utf-8")))
        self.assertEqual(list(codecs.iterdecode(expect, "utf-8")),
                         list(codecs.iterdecode(io.StringIO(expect), "utf-8")))

    def test_readbuffer_decode(self):
        expect = "abcdefghij"
        self.assertEqual(list(codecs.iterdecode(expect, "utf-8")),
                         list(codecs.iterdecode(io.BytesIO(expect), "utf-8")))
        self.assertEqual(list(codecs.iterdecode(expect, "utf-8")),
                         list(codecs.
