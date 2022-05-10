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

class Test_codec_error_handling(unittest.TestCase):
    def test_utf8_error_handling(self):
        # This test checks that the backslashreplace error handler
        # works correctly for the UTF-8 codec.
        #
        # UTF-8 is a tricky codec because it's stateful.
        #
        # We use the following invalid byte sequences:
        #
        #   - 0x80: continuation byte without a preceding start byte.
        #   - 0xc0 0x00: an overlong encoding of the NUL character.
        #   - 0xc0 0x80: an overlong encoding of the euro sign.
        #   - 0xe0 0x80 0x80: an overlong encoding of U+0000.
        #   - 0xe0 0x80 0x81: an overlong encoding of U+0001.
        #   - 0xf0 0x80 0x80 0x80: an overlong encoding of U+000000.
        #   - 0xf0 0x80 0x80 0x81: an overlong encoding of
