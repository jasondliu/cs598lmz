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

# Check that the codecs.register_error() function works.

# Test that the codecs.register_error() function works for
# UnicodeEncodeError and UnicodeDecodeError.

def test_unicode_errors(encoding):
    try:
        u"\U0010ffff".encode(encoding)
    except UnicodeEncodeError as exc:
        pass
    else:
        raise Exception("UnicodeEncodeError not raised")
    try:
        b"\xff\xff\xff\xff".decode(encoding)
    except UnicodeDecodeError as exc:
        pass
    else:
        raise Exception("UnicodeDecodeError not raised")

for encoding in "utf-8", "utf-16", "utf-32":
    test_unicode_errors(encoding)

# Test that the codecs.register_error() function works for
# UnicodeTranslateError.

def test_unicode_translate_error(encoding):
    try:
        u"\U0010ffff".encode(encoding, "replace")

