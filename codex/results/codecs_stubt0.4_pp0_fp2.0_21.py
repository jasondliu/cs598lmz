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
    # Test codecs.decode()
    assert codecs.decode("abc\xff", "ascii", "strict") == "abc\xff"
    assert codecs.decode("abc\xff", "ascii", "ignore") == "abc"
    assert codecs.decode("abc\xff", "ascii", "replace") == "abc?"
    assert codecs.decode("abc\xff", "ascii", "add_one_codepoint") == "abca"

    assert codecs.decode("abc\xff", "utf-16", "strict") == "\udcffabc"
    assert codecs.decode("abc\xff", "utf-16", "ignore") == "abc"
    assert codecs.decode("abc\xff", "utf-16", "replace") == "\ufffdabc"
    assert codecs.decode("abc\xff", "utf-16", "add_one_codepoint") == "abca"
    assert codecs.decode("abc\xff", "utf
