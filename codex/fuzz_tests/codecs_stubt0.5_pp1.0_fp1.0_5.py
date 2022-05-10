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
    if isinstance(input, str):
        input = input.encode(encoding)
    try:
        output = input.decode(encoding, error)
    except UnicodeDecodeError:
        raise
    except Exception as e:
        raise AssertionError("{} raised {}".format(error, e))
    assert output == expected, "{}({!r}) -> {!r} != {!r}".format(error, input, output, expected)

def test_add_one_codepoint():
    # invalid single byte
    check_error("utf-8", "add_one_codepoint", b'\xff', 'a\ufffd')
    check_error("utf-8", "add_one_codepoint", b'\xff\xff', 'a\ufffd\ufffd')
    check_error("utf-8", "add_one_codepoint", b'\xff\xff\xff', 'a\ufffd\ufffd\ufffd')
    check_
