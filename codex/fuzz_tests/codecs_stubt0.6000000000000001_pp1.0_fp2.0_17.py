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

# check the basic codec error handling functions

def test_decode():
    # test the default
    assert bytes.decode(b"abc\xff") == "abc\ufffd"
    # test the replace error handler
    assert bytes.decode(b"abc\xff", "replace") == "abc\ufffd"
    # test the ignore error handler
    assert bytes.decode(b"abc\xff", "ignore") == "abc"
    # test a custom error handler
    assert bytes.decode(b"abc\xff", "add_one_codepoint") == "abca"
    # test a custom error handler with a non-byte string
    assert bytes.decode(b"abc\xff", "add_utf16_bytes") == "ab\ufffd"
    # test a custom error handler with a non-byte string
    assert bytes.decode(b"abc\xff", "add_utf32_bytes") == "a"
    # test the xmlcharrefreplace error handler
    assert bytes.decode(b"abc\xff", "xmlcharrefreplace
