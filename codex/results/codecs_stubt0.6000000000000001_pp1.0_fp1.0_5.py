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

# The following test is actually a bit fragile, it assumes that the
# implementation uses the same number of bytes for the replacement as
# the number of bytes consumed by the bad byte.

# UnicodeUCS2
codecs.register_error("test", add_one_codepoint)
try:
    codecs.unicode_escape_decode(b'\x00\x00\x00\x00\x00\x00\x80\x00')
except UnicodeDecodeError as exc:
    print(exc, exc.object.decode("unicode_escape", "test"))

# UnicodeUTF8
codecs.register_error("test", add_one_codepoint)
try:
    codecs.unicode_escape_decode(b'\x00\x00\x00\x00\x00\x00\xc0\x80')
except UnicodeDecodeError as exc:
    print(exc, exc.object.decode("unicode_escape", "test"))

# UnicodeUTF16
codecs.register_error("test",
