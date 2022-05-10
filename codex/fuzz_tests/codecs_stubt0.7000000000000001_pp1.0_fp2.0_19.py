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

# All tests will be performed via the UTF-16 codec
encoding = "utf-16"

# For each test, we will have a list of input bytes and an expected
# error handler outcome.
tests = [
    # (input bytes, expected result)
    (b'\xff', '\ufffd'),
    (b'\xff\x00', '\ufffd\x00'),
    (b'\xff\x00\xff', '\ufffd\x00\ufffd'),
    (b'\xff\x00\xff\x00', '\ufffd\x00\ufffd\x00'),
    (b'\xff\x00\xff\x00\xff', 'a\x00\xff\x00\ufffd'),
    (b'\xff\x00\xff\x00\xff\x00', 'ab\x00\xff\x00\ufffd'),
    (b'\xff\x00\xff\x00\xff\x00\xff', 'ab\x00\xff\x00\ufffd\x00'),

