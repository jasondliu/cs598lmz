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

# Tests for invalid UTF-8

tests = [
    # invalid UTF-8 bytes
    (b'\xff', 'add_one_codepoint', 'a\ufffd'),
    (b'\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd'),
    (b'\xff\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd\ufffd'),
    (b'\xff\xff\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd\ufffd\ufffd'),
    (b'\xff\xff\xff\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd\ufffd\ufffd\ufffd'),
    (b'\xff\xff\xff\xff\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'),
    (b'\xff\xff\xff\xff\xff\xff\xff',
