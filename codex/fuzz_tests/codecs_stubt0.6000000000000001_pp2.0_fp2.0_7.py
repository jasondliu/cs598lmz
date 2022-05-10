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

# This is the range of codepoints that can be encoded in a single
# utf-16 character.
utf16_range = range(0x10000)

# This is the range of codepoints that can be encoded in a single
# utf-32 character.
utf32_range = range(0x110000)

# UTF-16 surrogate halves
surrogate_range = range(0xd800, 0xe000)

for cp in utf16_range:
    # UTF-16 surrogate halves are illegal in UTF-16
    if cp in surrogate_range:
        continue
    # U+FFFE and U+FFFF are illegal in UTF-16
    if cp in (0xfffe, 0xffff):
        continue
    # Make sure we can encode and decode a single codepoint in UTF-16
    assert codecs.utf_16_encode(cp) == (cp, 1)
    assert codecs.utf_16_decode(codecs.utf_16_encode(cp)[0]) == (cp, 1)
    # Make sure we
