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


class UnicodeEncodeErrorTest(unittest.TestCase):

    def test_basic(self):
        # on narrow builds, surrogates are always a failure, but on wide
        # builds, we can encode them if the codec allows it.
        # so we do an extra check for the surrogate, but only on wide builds.
        u = '\ud800'
        self.assertRaises(UnicodeEncodeError, u.encode, 'ascii')
        self.assertRaises(UnicodeEncodeError, u.encode, 'ascii', 'strict')
        u.encode('ascii', 'ignore')
        self.assertRaises(UnicodeEncodeError, u.encode, 'ascii', 'replace')
        u.encode('ascii', 'backslashreplace')
        u.encode('ascii', 'xmlcharrefreplace')
        if sys.maxunicode == 0x10ffff:
            # only check the surrogate on a wide build
            u.encode('utf-16')
            self.
