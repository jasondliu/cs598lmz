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

    def test_start_end(self):
        # Check that start and end are correctly set
        s = b'\xff\xff\xff\xff\xff'
        u = '\ufffd\ufffd\ufffd\ufffd\ufffd'
        e = UnicodeDecodeError('ascii', s, 1, 4, 'ouch')
        self.assertEqual(e.object, s)
        self.assertEqual(e.start, 1)
        self.assertEqual(e.end, 4)
        self.assertEqual(e.reason, 'ouch')
        self.assertEqual(e.encoding, 'ascii')
        self.assertEqual(e.args, ('ascii', s, 1, 4, 'ouch'))
        self.assertEqual(e.startswith('ouch'), True)
        self.assertEqual(e.endswith('ouch'), True)
        self.assertEqual(e.find('ouch'), 0)
        self
