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

class Test(unittest.TestCase):
    def test_utf8_decode(self):
        # Test UTF-8 decoding
        self.assertEqual('\u1234'.encode('utf-8').decode('utf-8', 'add_one_codepoint'), '\u1234a')
        self.assertEqual('\u1234'.encode('utf-8').decode('utf-8', 'add_utf16_bytes'), '\u1234ab')
        self.assertEqual('\u1234'.encode('utf-8').decode('utf-8', 'add_utf32_bytes'), '\u1234abcd')

    def test_utf16_decode(self):
        # Test UTF-16 decoding
        self.assertEqual('\u1234'.encode('utf-16').decode('utf-16', 'add_one_codepoint'), '\u1234a')
        self.assertEqual('\u1234'.encode('utf-16').decode('utf-16', 'add_
