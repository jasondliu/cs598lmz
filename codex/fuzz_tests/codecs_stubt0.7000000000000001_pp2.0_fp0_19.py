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

# Below are some tests for the surrogatepass error handler.
#
# The surrogatepass error handler replaces all unmatched UTF-16 surrogate
# code units by the Unicode replacement character U+FFFD.  All other
# codecs that handle UTF-16 correctly should generate the same output.

b1 = b'\xd8\x00'
b2 = b'\xd8'
b3 = b'\xdc\x00'
b4 = b'\xdc'
b5 = b'\xd8\x00\xd8\x00\xd8\x00\xd8\x00'
b6 = b'\xd8\x00\xd8\x00\xd8\x00\xd8'
b7 = b'\xd8\x00\xd8\x00\xdc\x00\xdc\x00'
b8 = b'\xd8\x00\xd8\x00\xdc\x00\xdc'
b9 = b'\xd8\x00\xd8\x00\xd8\x00\xd8
