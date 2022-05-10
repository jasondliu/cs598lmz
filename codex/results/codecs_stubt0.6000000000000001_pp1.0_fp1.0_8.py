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

#
#   U+0040
#
byte_string = b"\x40"
byte_string_with_null = b"\x40\x00"
byte_string_with_null_and_stuff = b"\x40\x00blah"

#
#   U+10400
#
utf16_string = b"\xd8\x40\xdc\x00"
utf16_string_with_null = b"\xd8\x40\xdc\x00\x00"
utf16_string_with_null_and_stuff = b"\xd8\x40\xdc\x00\x00blah"

#
#   U+10000
#
utf32_string = b"\x00\x01\x00\x00"
utf32_string_with_null = b"\x00\x01\x00\x00\x00"
utf32_string_with_null_and_stuff = b"\x00\x01\x00\x00\x00blah"

