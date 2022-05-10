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

    def test_start_pos(self):
        u = UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')
        self.assertEqual(u.start, 1)
        u.start = 42
        self.assertEqual(u.start, 42)

    def test_end_pos(self):
        u = UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')
        self.assertEqual(u.end, 2)
        u.end = 42
        self.assertEqual(u.end, 42)

    def test_object_attributes(self):
        # Verify that UnicodeDecodeError instances have an 'object' attribute
        # that always matches the string passed in to the constructor.
        u = UnicodeDecodeError('utf-8', b'\xff', 1, 2, '
