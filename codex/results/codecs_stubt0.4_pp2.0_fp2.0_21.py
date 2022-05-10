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

# In this test, we assume that the UTF-8 codec can decode any
# UTF-8 byte sequence.

def test_decode_utf8_surrogates():
    # Test decoding of UTF-8 with surrogates
    #
    # The surrogates must be decoded as surrogates, not as
    # replacement characters.
    #
    # The surrogates must not be decoded as UTF-8 bytes.
    #
    # The surrogates must be decoded as UTF-8 bytes when the
    # surrogatepass error handler is used.
    #
    # The surrogates must be decoded as UTF-8 bytes when the
    # surrogateescape error handler is used.
    #
    # The surrogates must be decoded as UTF-8 bytes when the
    # backslashreplace error handler is used.
    #
    # The surrogates must be decoded as UTF-8 bytes when the
    # namereplace error handler is used.
    #
    # The surrogates must be decoded as UTF-8 bytes when the
    # xmlcharrefreplace error handler is used.
    #
