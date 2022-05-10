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

    """
    # Basic tests, no errors
    try:
        # Test encoding
        assert ''.join(codecs.utf_32_encode(u"abc")) == b'\x00\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'
        assert ''.join(codecs.utf_32_encode(u"abc", 'strict')) == b'\x00\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'
        assert ''.join(codecs.utf_32_encode(u"abc", 'ignore')) == b'\x00\x00\x00a\x00\x00\x00b\x00\x00\x00c\x00\x00\x00'
        assert ''.join(codecs.utf_32_encode(u"abc", 'replace')) == b'\x
