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

test_list = [
    # invalid utf-16
    (b"\xff", "add_utf16_bytes"),
    (b"\xff\xff", "add_utf16_bytes"),
    (b"\xff\xff\xff", "add_utf16_bytes"),
    (b"\xff\xff\xff\xff", "add_utf16_bytes"),
    # invalid utf-32
    (b"\xff", "add_utf32_bytes"),
    (b"\xff\xff", "add_utf32_bytes"),
    (b"\xff\xff\xff", "add_utf32_bytes"),
    (b"\xff\xff\xff\xff", "add_utf32_bytes"),
    # invalid surrogate
    (b"\xed\xad\xb4\xed", "add_utf32_bytes"),
    (b"\xed\xad\xb4\xed\x8c\x80", "add_utf32_bytes"),
    (b"\xed\xad\xb4\x
