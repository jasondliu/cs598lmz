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

# Test the "add_one_codepoint" error handler.

# Test UTF-8.
# Test with a single-byte character in the middle.
s = b'abc\x80def'
print(s.decode("utf-8", "add_one_codepoint"))
# Test with a multi-byte character in the middle.
s = b'abc\xc2\x80def'
print(s.decode("utf-8", "add_one_codepoint"))

# Test UTF-16.
# Test with a single-byte character in the middle.
s = b'abcd\x80ef'
print(s.decode("utf-16", "add_one_codepoint"))
# Test with a multi-byte character in the middle.
s = b'abcd\xc2\x80ef'
print(s.decode("utf-16", "add_one_codepoint"))

# Test UTF-32.
# Test with a single-byte character in the middle.
s = b'abcdef\x80'
print
