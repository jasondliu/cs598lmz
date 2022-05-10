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

    def test_decode(self):
        self.assertEqual('abc', 'abc'.decode('ascii'))
        self.assertEqual('\xe9', '\xc3\xa9'.decode('utf-8'))
        self.assertEqual('\u1234', '\xe1\x88\xb4'.decode('utf-8'))
        self.assertEqual('\U00012345', '\xf0\x92\x8d\x85'.decode('utf-8'))
        self.assertEqual('\U00012345', '\xf0\x92\x8d\x85'.decode('utf-32-be'))
        self.assertEqual('\U00012345', '\x00\x00\x12\x34\x00\x00\x00\x00'.decode('utf-32-le'))
        self.assertEqual('\U00012345', '\x34\x12\x
