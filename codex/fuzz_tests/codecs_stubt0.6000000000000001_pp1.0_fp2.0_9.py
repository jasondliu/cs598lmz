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

# Non-ASCII characters
s = "\u20ac\u2039"

# Test all encodings
for encoding in encodings:
    # Test an encoding that supports the characters
    try:
        encoded = s.encode(encoding)
    except LookupError:
        continue
    except UnicodeEncodeError:
        continue
    except UnicodeTranslateError:
        continue

    # Test with replacement error handler
    encoded = s.encode(encoding, "replace")
    encoded = s.encode(encoding, "replace")
    encoded = s.encode(encoding, "replace")
    encoded = s.encode(encoding, "replace")

    # Test with backslashreplace error handler
    encoded = s.encode(encoding, "backslashreplace")
    encoded = s.encode(encoding, "backslashreplace")
    encoded = s.encode(encoding, "backslashreplace")
    encoded = s.encode(encoding, "backslashreplace")

    # Test with xmlcharrefreplace error
