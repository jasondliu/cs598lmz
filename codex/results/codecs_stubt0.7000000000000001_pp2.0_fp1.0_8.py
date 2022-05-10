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

class TestInput(unittest.TestCase):

    def test_utf8(self):
        # "ab" + "cdef" -> "abcdef"

        # single-byte replacement
        self.assertEqual(codecs.utf_8_decode("abcdef", "replace")[0],
                         "\x61\x62\x63\x64\x65\x66")

        self.assertEqual(codecs.utf_8_decode("ab\xed\xb0\x80cdef", "replace")[0],
                         "\x61\x62\xef\xbf\xbd\x63\x64\x65\x66")

        self.assertEqual(codecs.utf_8_decode("ab\xed\xb0\x80\xed\xb0\x80cdef", "replace")[0],
                         "\x61\x62\xef\xbf\xbd\xef\xbf\xbd\x63\x64\x65\x66")

        # single-byte
