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

class TestUnicodeDecodeError(unittest.TestCase):

    def test_init(self):
        # __init__(encoding, object, start, end, reason, msg='')
        exc = UnicodeDecodeError('encoding', b'obj', 0, 1, 'reason')
        self.assertEqual(exc.encoding, 'encoding')
        self.assertEqual(exc.object, b'obj')
        self.assertEqual(exc.start, 0)
        self.assertEqual(exc.end, 1)
        self.assertEqual(exc.reason, 'reason')
        self.assertEqual(exc.args, ('encoding', b'obj', 0, 1, 'reason'))
        self.assertEqual(exc.message, '')
        self.assertEqual(str(exc),
                         "'encoding' codec can't decode byte 0x6f in position 0: reason")

        exc = UnicodeDecodeError('encoding', b'obj', 0, 1, 'reason', 'message')
        self.assertE
