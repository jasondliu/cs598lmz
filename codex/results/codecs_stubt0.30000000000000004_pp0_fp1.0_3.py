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

class Test_UnicodeDecodeError(unittest.TestCase):

    def test_constructor(self):
        exc = UnicodeDecodeError('utf-8', b'\xff', 0, 1, 'ouch')
        self.assertEqual(exc.encoding, 'utf-8')
        self.assertEqual(exc.object, b'\xff')
        self.assertEqual(exc.start, 0)
        self.assertEqual(exc.end, 1)
        self.assertEqual(exc.reason, 'ouch')
        self.assertEqual(str(exc), "'utf-8' codec can't decode byte 0xff in position 0: ouch")

    def test_constructor_defaults(self):
        exc = UnicodeDecodeError('utf-8', b'\xff', 0, 1)
        self.assertEqual(exc.encoding, 'utf-8')
        self.assertEqual(exc.object, b'\xff')
        self.assertEqual(exc.start, 0)
        self.assertEqual(
