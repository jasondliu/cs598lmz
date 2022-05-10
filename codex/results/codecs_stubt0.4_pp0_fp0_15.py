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
    # test utf-16-le
    s = "abcd"
    s = s.encode("utf-16-le")
    s = s[:-1]
    s = s.decode("utf-16-le", "add_one_codepoint")
    assert s == "abcd", repr(s)

    # test utf-16-be
    s = "abcd"
    s = s.encode("utf-16-be")
    s = s[:-1]
    s = s.decode("utf-16-be", "add_one_codepoint")
    assert s == "abcd", repr(s)

    # test utf-32-le
    s = "abcd"
    s = s.encode("utf-32-le")
    s = s[:-1]
    s = s.decode("utf-32-le", "add_one_codepoint")
    assert s == "abcd", repr(s)

    # test utf-32-be

