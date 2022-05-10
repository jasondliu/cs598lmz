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

# bytes to str
unicode("\x80", "ascii", "add_one_codepoint")
unicode("\x80", "cp1252", "add_one_codepoint")
unicode(b'\x80\x80', "utf-16", "add_utf16_bytes")
unicode(b'\x80\x80\x80\x80', "utf-32", "add_utf32_bytes")

# bytes to str
str("\x80", "ascii", "add_one_codepoint")
str("\x80", "cp1252", "add_one_codepoint")
str(b'\x80\x80', "utf-16", "add_utf16_bytes")
str(b'\x80\x80\x80\x80', "utf-32", "add_utf32_bytes")

# unicode to str
str("\u1234", "ascii", "add_one_codepoint")
str("\u1234", "cp1252", "
