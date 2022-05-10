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

def test_utf16(s, expected):
    assert s.encode("utf-16") == expected
    assert s.encode("utf-16-le") == expected
    assert s.encode("utf-16-be") == expected
    assert s.encode("utf-16-ex") == expected
    assert s.encode("utf-16-ie") == expected
    assert s.encode("utf-16-le-ex") == expected
    assert s.encode("utf-16-be-ex") == expected
    assert s.encode("utf-16-ie-ex") == expected
    assert s.encode("utf-16-le-ie") == expected
    assert s.encode("utf-16-be-ie") == expected
    assert s.encode("utf-16-ie-ie") == expected
    assert s.encode("utf-16-le-ie-ex") == expected
    assert s.encode("utf-16-be-ie-ex") == expected
    assert s.encode("utf-16-ie-ie-ex
