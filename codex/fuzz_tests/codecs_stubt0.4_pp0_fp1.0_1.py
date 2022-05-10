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

class TestErrorHandling(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEqual('a\ud800'.encode('utf-8', 'add_one_codepoint'), b'a\xed\xa0\x80')
        self.assertEqual('a\udc00'.encode('utf-8', 'add_one_codepoint'), b'a\xed\xb0\x80')
        self.assertEqual('\ud800'.encode('utf-8', 'add_one_codepoint'), b'\xed\xa0\x80')
        self.assertEqual('\udc00'.encode('utf-8', 'add_one_codepoint'), b'\xed\xb0\x80')
        self.assertEqual('a\ud800\udc00'.encode('utf-8', 'add_one_codepoint'), b'a\xed\xa0\x80\xed\xb0\x80')
        self.
