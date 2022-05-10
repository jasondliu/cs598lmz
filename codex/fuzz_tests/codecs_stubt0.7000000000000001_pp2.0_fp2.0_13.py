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

def test_decode(encoding, input, expected):
    print(encoding, repr(input), repr(expected))
    actual = input.decode(encoding, "add_one_codepoint")
    assert actual == expected

def test_encode(encoding, input, expected):
    print(encoding, repr(input), repr(expected))
    actual = input.encode(encoding, "add_utf16_bytes")
    assert actual == expected

def test_lookup_error(encoding, input, expected):
    print(encoding, repr(input), repr(expected))
    try:
        actual = input.decode(encoding)
        raise RuntimeError("expected UnicodeDecodeError")
    except UnicodeDecodeError as e:
        assert e.args[1] == expected[0]

def test_lookup_error_encode(encoding, input, expected):
    print(encoding, repr(input), repr(expected))
    try:
        actual = input.encode(encoding)
        raise RuntimeError("expected
