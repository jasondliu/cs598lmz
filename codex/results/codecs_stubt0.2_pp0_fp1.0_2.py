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

class TestUTF8(unittest.TestCase):

    def test_utf8_decode_error(self):
        # Test that UTF-8 decoding errors are handled correctly.
        #
        # The UTF-8 decoder should raise a UnicodeDecodeError with
        # a start value of 1 when it encounters an invalid UTF-8
        # byte sequence.
        #
        # The UTF-8 decoder should raise a UnicodeDecodeError with
        # a start value of 2 when it encounters a valid UTF-8 byte
        # sequence that is too long.
        #
        # The UTF-8 decoder should raise a UnicodeDecodeError with
        # a start value of 4 when it encounters a valid UTF-8 byte
        # sequence that is too short.
        #
        # The UTF-8 decoder should raise a UnicodeDecodeError with
        # a start value of 5 when it encounters a valid UTF-8 byte
        # sequence that is too short.
        #
        # The UTF-8 decoder should raise a UnicodeDecodeError with
        # a start value of 6 when it encounters a
