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
        self.assertEqual(b'\x80'.decode('ascii', 'add_one_codepoint'), 'a\uFFFD')
        self.assertEqual('\uFFFD'.encode('ascii', 'add_one_codepoint'), b'a')

    def test_add_utf16_bytes(self):
        self.assertEqual(b'\x80'.decode('utf-16', 'add_utf16_bytes'), 'a\uFFFD')
        self.assertEqual('\uFFFD'.encode('utf-16', 'add_utf16_bytes'), b'ab')

    def test_add_utf32_bytes(self):
        self.assertEqual(b'\x80'.decode('utf-32', 'add_utf32_bytes'), 'a\uFFFD')
        self.assertEqual('\uFFFD'.encode('utf-32', 'add_
