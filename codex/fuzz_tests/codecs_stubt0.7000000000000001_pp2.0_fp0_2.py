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

class TestCodec(unittest.TestCase):
    def test_encode_utf8_errors(self):
        # encode
        self.assertEqual(u"\ud800".encode("utf-8", "strict"), b'\xf0\x90\x80\x80')
        self.assertEqual(u"\ud800".encode("utf-8", "replace"), b'?')
        self.assertEqual(u"\ud800".encode("utf-8", "ignore"), b'')
        self.assertEqual(u"\ud800".encode("utf-8", "backslashreplace"), b'\\ud800')
        self.assertEqual(u"\ud800".encode("utf-8", "xmlcharrefreplace"), b'&#55296;')
        self.assertEqual(u"\ud800".encode("utf-8", "add_one_codepoint"), b'a')
        self.assertEqual(u"\ud800".encode("utf-8", "add_utf
