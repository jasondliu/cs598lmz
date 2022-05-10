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

def test_main():
    # Test utf-8
    assert b'\xc3\xa9'.decode("utf-8", "add_one_codepoint") == 'a\xe9'
    assert b'\xc3\xa9'.decode("utf-8", "add_utf16_bytes") == 'a\xe9'
    assert b'\xc3\xa9'.decode("utf-8", "add_utf32_bytes") == 'a\xe9'

    # Test utf-16
    assert b'\xff\xfe\x00\xe9'.decode("utf-16", "add_one_codepoint") == 'a\xe9'
    assert b'\xff\xfe\x00\xe9'.decode("utf-16", "add_utf16_bytes") == 'a\xe9'
    assert b'\xff\xfe\x00\xe9'.decode("utf-16", "add_utf32_bytes") == 'a\xe9'

    # Test utf-32
    assert
