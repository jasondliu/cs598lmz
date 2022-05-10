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
    def test_encode(self):
        self.assertEqual(''.encode(), b'')
        self.assertEqual('abc'.encode(), b'abc')
        self.assertEqual('\u1234'.encode(), b'\xe1\x88\xb4')
        self.assertEqual('\U00012345'.encode(), b'\xf0\x92\x8d\x85')
        self.assertEqual('\u1234\U00012345'.encode(), b'\xe1\x88\xb4\xf0\x92\x8d\x85')

        self.assertEqual('abc'.encode('utf-8'), b'abc')
        self.assertEqual('abc'.encode('ascii'), b'abc')
        self.assertEqual('\u1234'.encode('utf-8'), b'\xe1\x88\xb4')
        self.assertEqual('\U00012345'.encode('
