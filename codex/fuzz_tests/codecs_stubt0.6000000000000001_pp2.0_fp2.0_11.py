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

# u'\uDC00' is a UTF-16 surrogate code point, and
# u'\U00010000' is a UTF-32 surrogate code point.
#
# Both are not valid UTF-8.

# add_one_codepoint
#
# This error handler adds one code point to the result
# string. This is not useful for UTF-8, as this would
# result in an invalid UTF-8 string.

# add_utf16_bytes
#
# This error handler adds two bytes to the result
# string. This is not useful for UTF-8, as this would
# result in an invalid UTF-8 string.

# add_utf32_bytes
#
# This error handler adds four bytes to the result
# string. This is not useful for UTF-8, as this would
# result in an invalid UTF-8 string.

# The following tests are expected to fail.

try:
    b"\xed\xb0\x80".decode("utf-8", "add_one_codepoint")
except UnicodeDecodeError as e:
   
