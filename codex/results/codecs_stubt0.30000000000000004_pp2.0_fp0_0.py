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

def test_utf16_decode_error(encoding):
    # Test that UTF-16 decoding errors are handled correctly.
    #
    # This test is a bit tricky, because UTF-16 is a variable-length encoding,
    # and the error can occur in the middle of a character.  We need to make
    # sure that the error handler is called with the correct position.
    #
    # We use the add_utf16_bytes error handler, which adds two bytes to the
    # input.  If the error occurs in the middle of a character, the error
    # handler will be called with a start value that is not a multiple of two.
    #
    # We use the add_one_codepoint error handler to make sure that the error
    # handler is called with the correct end value.
    #
    # We test all possible error positions, including the first and last bytes
    # of the input.
    #
    # We also test that an error in the middle of a character is handled
    # correctly.
    #
    # We test both little-endian and big-end
