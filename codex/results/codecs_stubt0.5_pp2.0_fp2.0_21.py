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

    def test_constructor(self):
        self.assertEqual(
            UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch').__dict__,
            {'encoding': 'utf-8', 'object': b'\xff', 'start': 1, 'end': 2,
             'reason': 'ouch'})
        self.assertEqual(
            UnicodeDecodeError('utf-8', b'\xff', 1, 2).__dict__,
            {'encoding': 'utf-8', 'object': b'\xff', 'start': 1, 'end': 2,
             'reason': None})

    def test_start_end(self):
        exc = UnicodeDecodeError('utf-8', b'\xff', 1, 2, 'ouch')
        self.assertEqual(exc.start, 1)
        self.assertEqual(exc.end, 2)

    def test_reason(self):
        exc = UnicodeDecodeError('utf-8',
