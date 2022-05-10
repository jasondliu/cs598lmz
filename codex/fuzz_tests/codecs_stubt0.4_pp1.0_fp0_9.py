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
    u"\u0100".encode("ascii", "add_one_codepoint")
except UnicodeEncodeError as uee:
    print("add_one_codepoint:", uee)

try:
    u"\u0100".encode("utf-16", "add_utf16_bytes")
except UnicodeEncodeError as uee:
    print("add_utf16_bytes:", uee)

try:
    u"\u0100".encode("utf-32", "add_utf32_bytes")
except UnicodeEncodeError as uee:
    print("add_utf32_bytes:", uee)
