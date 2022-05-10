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

def test_error_handling(input, errors, expected):
    output = input.encode("utf-8", errors)
    print("input:", repr(input))
    print("output:", repr(output))
    print("expected:", repr(expected))
    assert output == expected

test_error_handling("abc\ud800def", "add_one_codepoint", b"abcaef")
test_error_handling("abc\ud800def", "add_utf16_bytes", b"abca\x00def")
test_error_handling("abc\ud800def", "add_utf32_bytes", b"abca\x00\x00\x00def")

test_error_handling("abc\ud800def", "replace", b"abcef")
test_error_handling("abc\ud800def", "ignore", b"abcdef")
test_error_handling("abc\ud800def", "xmlcharrefreplace", b"abc&#65536;def")

test_error_handling("abc\
