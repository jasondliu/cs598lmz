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

# Make sure that the surrogatepass handler doesn't decode the
# surrogates to the codepoints they represent.

# The surrogatepass handler will just pass through the surrogate
# values.  This means that the bytes written to the output file should
# be the same as the bytes read from the input file.

# The first surrogate is U+DC00, which is 0xDC00 in UTF-32, 0xDC00 in
# UTF-16, and 0xED 0xB0 0x80 in UTF-8.  The second surrogate is U+D800,
# which is 0xD800 in UTF-32, 0xD800 in UTF-16, and 0xED 0xA0 0x80 in
# UTF-8.  The code point represented by both surrogates is U+10400,
# which is 0x00010400 in UTF-32, 0xD801 0xDC00 in UTF-16, and 0xF0
# 0x90 0x90 0x80 in UTF-8.

# The surrogatepass handler should decode the first surrogate to the
# first surrogate, and the second
