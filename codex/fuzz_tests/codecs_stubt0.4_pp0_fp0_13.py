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

# Test decoder

def test_decoder_error_handling():
    # Test that the decoder handles decoding errors correctly.
    # This test is for the code in unicodeobject.c::unicode_decode_call_errorhandler
    # (called from unicode_decode_call_errorhandler)
    #
    # The test works by feeding the decoder a byte sequence that cannot be decoded.
    # The error handler is supposed to return a replacement string, and the decoder
    # should continue decoding after that point.
    #
    # The test is run for each of the following codecs:
    #   - utf-8
    #   - utf-16-le
    #   - utf-16-be
    #   - utf-32-le
    #   - utf-32-be
    #
    # The error handler is called with a different error object for each of the codecs,
    # and the error handler returns a different replacement string for each codec.
    #
    # For utf-8, the error handler is called with a
