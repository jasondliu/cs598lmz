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

# The byte strings to be encoded
encodable_bytes_strs = [
    b"abcd",
    b"\x00\x01\xfe\xff",
    b"\xff\xfe\x00\x00",
    b"\x00\x00\xfe\xff",
    b"\xff\xfe\x00\x01",
    b"\xff\xfe\xff\xff",
    b"\x00\x00\x00\x00",
    b"\x7f\x7f\x7f\x7f",
    b"\x80\x80\x80\x80",
    ]

# The unambiguous code point to UTF-16-BE encodings
utf16_bytes_strs = [
    b"abcd",               # "\u0abc\ud800"
    b"\x00\x01\xfe\xff",   # "\u0001\ufffe"
    b"\xff\xfe\x00\x00",   # "\ufffe\u
