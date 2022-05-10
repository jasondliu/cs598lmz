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

def check_error_handler(input, handler, expected):
    decoder = codecs.getincrementaldecoder(encoding)(handler)
    actual = decoder.decode(input, True)
    print("input: %a" % (input,))
    print("output: %a" % (actual,))
    print("expected: %a" % (expected,))
    assert actual == expected

def check_utf8_error_handler(input, handler, expected):
    check_error_handler(input, handler, expected)
    check_error_handler(bytearray(input), handler, expected)

def check_utf16_error_handler(input, handler, expected):
    check_error_handler(input, handler, expected)
    check_error_handler(bytearray(input), handler, expected)

def check_utf32_error_handler(input, handler, expected):
    check_error_handler(input, handler, expected)
    check_error_handler(bytearray(input), handler, expected)

print("check
