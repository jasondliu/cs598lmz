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

print(b'hi\x80\x80world'.decode("ascii", "add_one_codepoint"))
print(b'\xfe\xff\x2c\x00\x2e'.decode("utf16", "add_utf16_bytes"))
print(b'\xff\xfe\x00\x00\x00\x2c\x00\x00\x00\x2e'.decode("utf32", "add_utf32_bytes"))

def add_one_codepoint_encode(exc):
    return ("a", exc.start)

def add_utf16_bytes_encode(exc):
    return (b'\x00a', exc.start)

def add_utf32_bytes_encode(exc):
    return (b'\x00\x00\x00a', exc.start)

def add_raw_bytes(exc):
    return (b'a', exc.start)

codecs.register_error("add_one_codepoint_encode", add
