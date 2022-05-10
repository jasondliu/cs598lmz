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

# Some tests for codecs.escape_decode()

import codecs

def test_escape_decode():
    assert codecs.escape_decode(b'abc') == (b'abc', 3)
    assert codecs.escape_decode(b'\\a') == (b'\a', 2)
    assert codecs.escape_decode(b'\\x01') == (b'\x01', 4)
    assert codecs.escape_decode(b'\\u1234') == (b'\u1234', 6)
    assert codecs.escape_decode(b'\\U00012345') == (b'\U00012345', 10)
    assert codecs.escape_decode(b'\\U00012345', 'replace') == (b'\ufffd', 10)
    assert codecs.escape_decode(b'\\U00012345', 'ignore') == (b'', 10)
    assert codecs.escape_decode(b'\\U00012345', 'backslashreplace') == (b'\\
