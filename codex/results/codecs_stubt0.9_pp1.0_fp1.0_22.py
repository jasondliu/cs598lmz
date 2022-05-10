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

# If a surrogate is present, the old codecs mechanism encode()/symbol
# function would raise a UnicodeEncodeError, while our code will encode
# the input by raising UnicodeTranslateError that contains the single
# surrogate.
for ucs2, utf16 in ("\U00010001", "\ud800\udc01", "\\U00010001", "\\ud800\\udc01"):
    try:
        utf16.encode("utf-16")
    except UnicodeTranslateError as exc:
        pass
    else:
        print("FAILED: single surrogate", repr(ucs2))

for ucs4, utf32 in ("\U00010000", "\ud800\udc00", "\\U00010000", "\\ud800\\udc00"):
    try:
        utf32.encode("utf-32")
    except UnicodeTranslateError as exc:
        pass
    else:
        print("FAILED: single surrogate", repr(ucs2))

# Error handler that replaces the original byte byte sequence
# with a single character.
