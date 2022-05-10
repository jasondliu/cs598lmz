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

def test(encoding, errors):
    try:
        s = bytes(range(0x110000)).decode(encoding, errors)
    except UnicodeDecodeError as exc:
        print("UnicodeDecodeError:", exc)
    except UnicodeTranslateError as exc:
        print("UnicodeTranslateError:", exc)
    else:
        print("OK")

# Test all codecs that support errors="replace".
for encoding in dir(codecs):
    if encoding.endswith("_errors"):
        continue
    try:
        codecs.lookup(encoding).decode(b"", errors="strict")
    except LookupError:
        continue
    except TypeError:
        continue
    print(encoding, end=' ')
    test(encoding, "replace")
    print(encoding, end=' ')
    test(encoding, "add_one_codepoint")
    print(encoding, end=' ')
    test(encoding, "add_utf16_bytes")
    print(
