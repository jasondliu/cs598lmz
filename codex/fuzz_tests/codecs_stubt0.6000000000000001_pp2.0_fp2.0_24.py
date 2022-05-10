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

def test(encoding):
    print(encoding, end=' ')
    try:
        codecs.lookup_error(encoding)
    except LookupError:
        print("not supported")
    else:
        print()
        for error in ("strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            print(" ", error, end=' ')
            try:
                codecs.lookup_error(error)
            except LookupError:
                print("not supported")
            else:
                print()
                try:
                    u"\u3042".encode(encoding, error)
                except UnicodeEncodeError as exc:
                    print("  ", exc.start, exc.end, exc.object[exc.start:exc.end])
                else:
                    print("  no error")

for encoding in ("ascii", "latin-1", "utf-8", "utf-16", "utf-32"):
    test(encoding
