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
    assert codecs.decode("abc", "ascii") == "abc"
    assert codecs.decode(b"abc", "ascii") == "abc"
    assert codecs.decode(b"abc", "ascii", "strict") == "abc"
    assert codecs.decode(b"abc", "ascii", "ignore") == "abc"
    assert codecs.decode(b"abc", "ascii", "replace") == "abc"
    assert codecs.decode(b"abc", "ascii", "add_one_codepoint") == "aabc"
    assert codecs.decode(b"abc", "ascii", "add_utf16_bytes") == "aabc"
    assert codecs.decode(b"abc", "ascii", "add_utf32_bytes") == "aabc"
    assert codecs.decode(b"abc", "ascii", "surrogateescape") == "
