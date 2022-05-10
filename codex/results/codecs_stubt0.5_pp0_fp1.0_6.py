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

codecs.register_error("test_decode_error", codecs.ignore_errors)
codecs.register_error("test_encode_error", codecs.ignore_errors)

# Also test the undocumented API for passing in a replacement string
# as a keyword argument instead of a tuple.
class ReplaceStringError(UnicodeError):
    def __init__(self, encoding, reason, object, start, end, replacement=None):
        UnicodeError.__init__(self, encoding, reason, object, start, end)
        self.replacement = replacement

def replace_string(exc):
    return (exc.replacement, exc.start, exc.end)

codecs.register_error("replace_string", replace_string)

class CodecTest(unittest.TestCase):
    def test_basics(self):
        self.assertEqual("abc", codecs.encode("abc", 'ascii'))
        self.assertEqual("abc", codecs.decode(b"abc", 'ascii'))
        self
