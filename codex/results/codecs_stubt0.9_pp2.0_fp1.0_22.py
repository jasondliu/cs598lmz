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

class CodecTest(unittest.TestCase):
    '''Test Unicode codecs (encodings).'''
    encoding = 'test' # set in subclass

    def setUp(self):
        self.errors = []
        self.errorcall = 0

    def test_getregentry(self):
        try:
            e = codecs.getregentry(self.encoding)
        except LookupError:
            # Encoding not found. Skip the rest of the tests.
            return
        self.assertTrue(callable(e.encode))
        self.assertTrue(callable(e.decode))

    @requires_unicode_support
    def test_basicencoding(self):
        for i in range(len(xrange2codec)):
            u = xrange2unicode[i]
            if not u:
                self.assertRaises(UnicodeError, self.encode, u, self.encoding)
            else:
                s = self.encode(u, self.encoding)
                self.assertEqual(
