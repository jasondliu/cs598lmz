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

def test_unicode_decode_error():
    u = chr(0xdc00)
    utf16 = u.encode("utf-16")
    assert utf16 == b'\x00\xdc'

    # Test that a UnicodeDecodeError is raised
    with pytest.raises(UnicodeDecodeError, match="utf-8"):
        utf16.decode('utf-8')

    # Test that adding a replacement codepoint solves it
    result = utf16.decode('utf-8', 'replace')
    assert result == u'\ufffd'

    # Test that adding one codepoint works
    result = utf16.decode('utf-8', 'add_one_codepoint')
    assert result == u'a'

    # Test that adding two UTF-16 bytes works
    result = utf16.decode('utf-8', 'add_utf16_bytes')
    assert result == u'a\udccc'

    # Test that adding four UTF-16 bytes works
    result = ut
