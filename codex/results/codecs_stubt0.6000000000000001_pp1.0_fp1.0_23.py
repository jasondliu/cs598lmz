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

# Bug #1923: UTF-16-LE codec should not accept BOM-less UTF-16-BE
try:
    codecs.utf_16_le_decode(b'\xfe\xff\x00\x61')
except UnicodeError:
    pass
else:
    raise Exception("decoding BOM-less UTF-16-BE as UTF-16-LE must fail")

# Bug #1923: UTF-16-LE codec should not accept BOM-less UTF-16-BE
try:
    codecs.utf_16_be_decode(b'\xff\xfe\x61\x00')
except UnicodeError:
    pass
else:
    raise Exception("decoding BOM-less UTF-16-LE as UTF-16-BE must fail")

# Bug #1923: UTF-16-LE codec should not accept BOM-less UTF-16-BE
try:
    codecs.utf_16_le_decode(b'\xff\xfe\x61\x00')
except UnicodeError:
    pass
else:

