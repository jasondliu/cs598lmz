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

# test codecs
for encoding in ("utf-8", "utf-16", "utf-32"):
    print("testing", encoding)
    for errors in ("add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
        print("\t", errors)
        try:
            codecs.decode(b'\xff', encoding, errors)
        except UnicodeDecodeError as exc:
            print("\t\t", exc)
            print("\t\t", codecs.decode(b'\xff', encoding, errors), errors)

# test str
for errors in ("add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
    print("testing", errors)
    try:
        "".encode("utf-8", errors)
    except UnicodeEncodeError as exc:
        print("\t", exc)
        print("\t", "".encode("utf-8", errors), errors)
