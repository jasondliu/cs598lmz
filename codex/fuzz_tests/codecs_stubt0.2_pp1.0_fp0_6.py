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

def test_utf8_decode(encoding):
    # Test that UTF-8 decoding errors are handled correctly.
    #
    # The UTF-8 decoder should raise a UnicodeDecodeError when it
    # encounters an invalid byte sequence.  The start attribute of the
    # exception object should be set to the start of the invalid byte
    # sequence, and the end attribute should be set to the end of the
    # invalid byte sequence.
    #
    # The reason attribute of the exception object should be set to
    # "invalid start byte" when the first byte of an invalid byte
    # sequence is an unexpected continuation byte.  The reason
    # attribute should be set to "unexpected code byte" when the first
    # byte of an invalid byte sequence is not a valid start byte or
    # continuation byte.
    #
    # The object attribute of the exception object should be set to
    # the byte string that was being decoded.
    #
    # The test_utf8_decode() function takes an encoding name as its
    # only argument.  The function decodes a series of byte
