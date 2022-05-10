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

class TestDecode(unittest.TestCase):

    def test_decode_error_handling(self):
        # Test that the error handling for decoding works as expected.
        # This is a bit tricky because the error handling is done in
        # C, not Python.
        #
        # The tests are done by first encoding a string with a known
        # encoding, then changing some of the bytes in the resulting
        # bytestring.  The decoder should then raise a UnicodeDecodeError
        # telling which byte was the cause of the problem.
        #
        # The tricky part is that the byte position in the error object
        # is not the byte index in the bytestring, but the byte index
        # starting from the beginning of the string.  This means that
        # the error position is moved forward each time a multi-byte
        # character is encountered.
        #
        # The error handler can signal failure by re-raising the
        # exception, or by returning a tuple with a replacement string
        # and the new position.  The new position is allowed to be past
        # the
