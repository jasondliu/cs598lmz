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

def check_add_one_codepoint(name, encoding, input, output):
    assert codecs.decode(input, encoding, "add_one_codepoint") == output

def check_add_utf16_bytes(name, encoding, input, output):
    assert codecs.decode(input, encoding, "add_utf16_bytes") == output

def check_add_utf32_bytes(name, encoding, input, output):
    assert codecs.decode(input, encoding, "add_utf32_bytes") == output

def check_add_one_codepoint_with_utf16_bytes(name, encoding, input, output):
    assert codecs.decode(input, encoding, "add_utf16_bytes") == output

def check_add_one_codepoint_with_utf32_bytes(name, encoding, input, output):
    assert codecs.decode(input, encoding, "add_utf32_bytes") == output

def check_add_utf16_bytes_with_utf32_bytes(name, encoding
