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

# test the codecs module

# test the UTF-8 codec

def test_utf8(test_string, test_unicode):
    # test the UTF-8 codec
    assert test_string.decode("utf-8") == test_unicode
    assert test_unicode.encode("utf-8") == test_string

    # test the UTF-8-SIG codec
    assert test_string.decode("utf-8-sig") == test_unicode
    assert test_unicode.encode("utf-8-sig") == test_string

    # test the UTF-16 codec
    assert test_string.decode("utf-16") == test_unicode
    assert test_unicode.encode("utf-16") == test_string

    # test the UTF-16-LE codec
    assert test_string.decode("utf-16-le") == test_unicode
    assert test_unicode.encode("utf-16-le") == test_string

    # test the UTF-16-BE codec
    assert test_string.
