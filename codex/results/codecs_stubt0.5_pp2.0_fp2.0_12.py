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

# This is the UTF-8 encoding of U+1D11E, which is not a valid Unicode
# scalar value.
invalid_utf8 = b'\xF0\x9D\x84\x9E'

# This is the UTF-16 big-endian encoding of U+1D11E, which is not a
# valid Unicode scalar value.
invalid_utf16_be = b'\xD8\x34\xDD\x1E'

# This is the UTF-16 little-endian encoding of U+1D11E, which is not a
# valid Unicode scalar value.
invalid_utf16_le = b'\x34\xD8\x1E\xDD'

# This is the UTF-32 big-endian encoding of U+1D11E, which is not a
# valid Unicode scalar value.
invalid_utf32_be = b'\x00\x00\xD8\x34\xDD\x1E'

# This is the UTF-32 little-endian encoding
