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
        UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')

    def test_str(self):
        self.assertEqual(str(UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')),
                         "('utf-8', b'\\xff', 1, 2, 'ouch')")

    def test_unicode(self):
        self.assertEqual(str(UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')),
                         "('utf-8', b'\\xff', 1, 2, 'ouch')")

    def test_repr(self):
        self.assertEqual(repr(UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')),
                         "UnicodeDecodeError('utf-8', b'\\xff', 1, 2, 'ouch')")

    def test_str
