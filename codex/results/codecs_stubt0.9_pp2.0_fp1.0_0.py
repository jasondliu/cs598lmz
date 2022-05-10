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

class CodecsExceptionTests(unittest.TestCase):

    def test_unicode_decode_error(self):
        self.check_unicode_exception(
            UnicodeDecodeError, "ascii",
            bytes(b"\xff"), 0, 1, "ordinal not in range(128)")

        self.check_unicode_exception(
            UnicodeDecodeError, "ascii",
            bytes(b"\xff\xff"), 0, 2, "ordinal not in range(128)")

        self.check_unicode_exception(
            UnicodeDecodeError, "ascii",
            bytes(b"a\xffb"), 1, 2, "ordinal not in range(128)")

        self.check_unicode_exception(
            UnicodeDecodeError, "ascii",
            bytes(b"a\xff\xffb"), 1, 3, "ordinal not in range(128)")

        self.check_unicode_exception(
            UnicodeDecodeError, "ascii",
            bytes(
