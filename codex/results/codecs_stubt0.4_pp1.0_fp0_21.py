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

# Test UTF-16 codec

decode_error = 0

def decode_utf16_error(exc):
    global decode_error
    decode_error = 1
    return ("", exc.start)

codecs.register_error("decode_utf16_error", decode_utf16_error)

decode_error = 0
u = codecs.decode("\xff\xfe\x00\x00\x00\x00\x00\x00", "utf-16", "decode_utf16_error")
assert decode_error

# Test UTF-32 codec

decode_error = 0

def decode_utf32_error(exc):
    global decode_error
    decode_error = 1
    return ("", exc.start)

codecs.register_error("decode_utf32_error", decode_utf32_error)

decode_error = 0
u = codecs.decode("\xff\xfe\x00\x00\x00\x00\x00\x00", "utf-32
