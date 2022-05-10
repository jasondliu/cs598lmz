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

# Test decoding

def test_decoding():
    # Test decoding with errors
    #
    # This tests the following error handlers:
    #   xmlcharrefreplace, backslashreplace, namereplace,
    #   add_one_codepoint, add_utf16_bytes, add_utf32_bytes
    #
    # The following codecs are tested:
    #   utf-8, utf-16, utf-16-be, utf-16-le, utf-32, utf-32-be, utf-32-le
    #
    # The following errors are tested:
    #   UnicodeDecodeError, UnicodeTranslateError
    #
    # The following error handler combinations are tested:
    #   strict, ignore, replace, xmlcharrefreplace, backslashreplace,
    #   namereplace, add_one_codepoint, add_utf16_bytes, add_utf32_bytes
    #
    # The following error handler combinations are not tested:
    #   strict + add_utf16_bytes, strict + add_utf32
