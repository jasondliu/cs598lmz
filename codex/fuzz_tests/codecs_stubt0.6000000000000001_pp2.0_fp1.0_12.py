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

# the code point is in the BMP
codecs.decode("\xFF", "iso8859-1", "add_one_codepoint")
# the code point is out of the BMP
codecs.decode("\xFF", "utf-16", "add_one_codepoint")
# the code point is in the BMP
codecs.decode("\xFF", "utf-32", "add_one_codepoint")

# the code point is in the BMP
codecs.decode(b'\xFF', "iso8859-1", "add_utf16_bytes")
# the code point is out of the BMP
codecs.decode(b'\xFF', "utf-16", "add_utf16_bytes")
# the code point is in the BMP
codecs.decode(b'\xFF', "utf-32", "add_utf16_bytes")

# the code point is in the BMP
codecs.decode(b'\xFF', "iso88
