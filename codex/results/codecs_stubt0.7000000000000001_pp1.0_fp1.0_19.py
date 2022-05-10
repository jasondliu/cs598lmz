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

class UnicodeErrorTests(unittest.TestCase):
    def test_basics(self):
        ue = UnicodeEncodeError('ascii', 'a', 0, 1, 'ordinal not in range')
        self.assertEqual(str(ue),
             " 'ascii' codec can't encode character 'a' in position 0: ordinal not in range(128)")
        self.assertEqual(repr(ue),
             "UnicodeEncodeError('ascii', 'a', 0, 1, 'ordinal not in range(128)')")
        ue = UnicodeEncodeError('ascii', 'a', 0, 1, 'ordinal not in range(128)')
        self.assertEqual(str(ue),
             " 'ascii' codec can't encode character 'a' in position 0: ordinal not in range(128)")
        self.assertEqual(repr(ue),
             "UnicodeEncodeError('ascii', 'a', 0, 1, 'ordinal not in range(128)')
