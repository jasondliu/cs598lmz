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

class TestUtf8(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEquals('a', '\uFFFE'.encode('utf-8', 'add_one_codepoint'))

    def test_add_utf16_bytes(self):
        # The UTF16 error handler should always return a UTF-16 byte string
        # that is valid.
        self.assertEquals('\uFFFE'.encode('utf-8', 'add_utf16_bytes'), b'ab')

    def test_add_utf32_bytes(self):
        # The UTF32 error handler should always return a UTF-32 byte string
        # that is valid.
        self.assertEquals('\uFFFE'.encode('utf-8', 'add_utf32_bytes'), b'abcd')

class TestUtf16(unittest.TestCase):
    def test_add_one_codepoint(self):
        self.assertEquals('a', '\uFFFE'.encode('utf-
