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

def check_error(encoding, error, input, expected):
    try:
        s = input.decode(encoding)
    except UnicodeDecodeError as e:
        s = e.object.decode(encoding, errors=error)
    if s != expected:
        print("Failed to decode %s with error handler %s" % (encoding, error))
        print("Input: %s" % input)
        print("Expected: %s" % expected)
        print("Got: %s" % s)
        raise AssertionError

def test_main():
    check_error("ascii", "ignore", b"abc\xffdef", "abcdef")
    check_error("ascii", "replace", b"abc\xffdef", "abc?def")
    check_error("ascii", "xmlcharrefreplace", b"abc\xffdef", "abc&#255;def")
    check_error("ascii", "backslashreplace", b"abc\xffdef", "abc\\xffdef")
    check_error
