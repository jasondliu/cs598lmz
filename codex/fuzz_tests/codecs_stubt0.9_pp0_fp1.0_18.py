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

try:
    unicode(1, "utf-8", "add_one_codepoint")
except TypeError:
    pass

try:
    unicode(b'a', "utf-8", "add_one_codepoint")
except TypeError:
    pass

try:
    unicode(b'a\x00\x00', "utf-32", "add_utf8_char")
except TypeError:
    pass

try:
    unicode(b'a\x00\x00', "utf-16", "add_utf8_char")
except TypeError:
    pass

unicode(b'a\x00\x00', "utf-16", "add_utf32_bytes")
unicode(b'a', "utf-32", "add_utf8_char")
