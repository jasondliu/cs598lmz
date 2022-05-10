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

class UnicodeDecodeErrorTest(unittest.TestCase):

    def test_init(self):
        UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'ouch')

    def test_start(self):
        u = UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'ouch')
        self.assertEqual(u.start, 0)
        u = UnicodeDecodeError('utf-8', b'\xff', 7, 8, 'ouch')
        self.assertEqual(u.start, 7)

    def test_end(self):
        u = UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'ouch')
        self.assertEqual(u.end, 1)
        u = UnicodeDecodeError('utf-8', b'\xff', 7, 8, 'ouch')
        self.assertEqual(u.end, 8)

    def test_reason(self):
        u = UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'ouch
