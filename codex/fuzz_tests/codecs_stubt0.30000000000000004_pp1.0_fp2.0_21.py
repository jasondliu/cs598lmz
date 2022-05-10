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

class Test_ErrorHandlers(unittest.TestCase):

    def test_surrogatepass(self):
        # surrogatepass error handler
        self.assertEqual(
            u"\ud800\udc00".encode("utf-8", "surrogatepass"),
            b"\xf0\x90\x80\x80"
        )
        self.assertEqual(
            u"\ud800\udc00".encode("utf-16", "surrogatepass"),
            b"\x00\xd8\x00\xdc"
        )
        self.assertEqual(
            u"\ud800\udc00".encode("utf-32", "surrogatepass"),
            b"\x00\x00\x00\xd8\x00\x00\x00\xdc"
        )
        self.assertEqual(
            u"\ud800\udc00".encode("utf-16-le", "surrogatepass"),
            b"\xd8\x00\xdc\
