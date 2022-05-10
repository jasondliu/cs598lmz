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

def test_decode_error(encoding, error_handler, expected_result):
    # Test that the error handler is called with the correct exception
    # type and that the result of the handler is used as the replacement
    # for the unencodable character.
    #
    # The error handler is called with a UnicodeEncodeError instance
    # for encodings that encode to Unicode, and a UnicodeDecodeError
    # instance for encodings that decode from Unicode.
    #
    # The expected_result is a tuple of the expected exception type
    # and the expected result of the error handler.
    #
    # The error handler is called with a UnicodeEncodeError instance
    # for encodings that encode to Unicode, and a UnicodeDecodeError
    # instance for encodings that decode from Unicode.
    #
    # The expected_result is a tuple of the expected exception type
    # and the expected result of the error handler.
    #
    # The error handler is called with a UnicodeEncodeError instance
    # for encodings that encode to Unicode, and a UnicodeDecode
