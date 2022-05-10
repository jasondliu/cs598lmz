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

class TestUTF16(unittest.TestCase):
    def test_utf16_exception(self):
        self.assertEqual(codecs.utf_16_exception_handler(u'\udc00'), (u'\ufffd', 1))
        self.assertEqual(codecs.utf_16_exception_handler(u'\ud800'), (u'\ufffd\ufffd', 1))
        self.assertEqual(codecs.utf_16_exception_handler(u'\ud800a'), (u'\ufffd\ufffda', 1))
        self.assertEqual(codecs.utf_16_exception_handler(u'\ud800\udc00'), (u'\U00010000', 1))
        self.assertEqual(codecs.utf_16_exception_handler(u'\ud800\udc00a'), (u'\U00010000a', 1))
        self.assertEqual(codecs.utf_16_exception_handler(u'\udc00
