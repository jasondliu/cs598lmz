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

def test_codecs():
    # Test that codecs.decode() and codecs.encode() work
    # correctly with the error handling callback functions.
    #
    # The following test cases are not covered by the standard
    # test suite:
    #   - decoding UTF-8 with a callback function for decoding
    #     errors
    #   - decoding UTF-16 with a callback function for encoding
    #     errors
    #   - decoding UTF-32 with a callback function for encoding
    #     errors
    #   - encoding UTF-8 with a callback function for encoding
    #     errors
    #   - encoding UTF-16 with a callback function for decoding
    #     errors
    #   - encoding UTF-32 with a callback function for decoding
    #     errors
    #
    # The following test cases are covered by the standard test
    # suite:
    #   - decoding UTF-8 with a callback function for encoding
    #     errors
    #   - decoding UTF-16 with a callback function for decoding
    #     errors
    #   - decoding UTF-32 with a callback function
