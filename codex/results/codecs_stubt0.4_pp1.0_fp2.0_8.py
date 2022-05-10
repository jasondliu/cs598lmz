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

# test unicode

for encoding in ('utf-8', 'utf-16', 'utf-32'):
    print("testing", encoding)
    for i in range(1, 4):
        print("  with", i, "errors")
        s = "a" * i
        try:
            s.encode(encoding)
        except UnicodeEncodeError as exc:
            print("    exception:", str(exc))
            s2 = s.encode(encoding, "add_one_codepoint")
            print("    add_one_codepoint:", repr(s2))
            s2 = s.encode(encoding, "add_utf16_bytes")
            print("    add_utf16_bytes:", repr(s2))
            s2 = s.encode(encoding, "add_utf32_bytes")
            print("    add_utf32_bytes:", repr(s2))
        else:
            print("    no exception")

# test bytes

for encoding in ('utf-8', 'utf-16', '
