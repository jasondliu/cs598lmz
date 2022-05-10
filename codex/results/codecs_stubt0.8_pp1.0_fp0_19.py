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

# Translate the illegal UTF-8 character "\x81" into "\u1234".
# This shouldn't raise a TypeError when the codecs.escape_encode()
# method is called with output_encoding="utf-16".
print(codecs.charmap_encode(b"\x81", "\x81", errors="add_one_codepoint"))

# Decoding the illegal UTF-16 bytes b"\x81\x81" should not raise a
# TypeError when the codecs.escape_decode() method is called with
# output_encoding="utf-8".
print(codecs.charmap_decode(b"\x81\x81", "\u20ac", errors="add_utf16_bytes"))

# Decoding the illegal UTF-32 bytes b"\x81\x81\x81\x81" should not raise a
# TypeError when the codecs.escape_decode() method called with
# output_encoding="utf-8".
print(codecs.charmap_decode(b"\x
