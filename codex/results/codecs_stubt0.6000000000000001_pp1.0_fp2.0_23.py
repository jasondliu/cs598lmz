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

def test_utf_16_be():
    # This test is written to test the UTF-16-BE codec.
    # The UTF-16-BE codec is tested by the test_unicode test
    # suite.
    #
    # UTF-16-BE encodes to UTF-16-BE, and decodes from UTF-16-BE.
    #
    # UTF-16-BE decodes from UTF-16-LE if the BOM is present.
    #
    # UTF-16-BE encodes to UTF-16-LE if the BOM is present.
    #
    # UTF-16-BE can decode from UTF-8, but only if the BOM is present.
    #
    # UTF-16-BE can encode to UTF-8, but only if the BOM is present.
    #
    # The UTF-16-BE codec can be used as a UTF-16 codec if the BOM is present.
    #
    # The UTF-16-BE codec can be used as a UTF-16 codec if the BOM is not
    # present.
    #
   
