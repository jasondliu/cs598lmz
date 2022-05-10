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
    print("codec:", encoding)
    for errors in ["strict", "replace", "ignore", "backslashreplace",
                   "xmlcharrefreplace", "add_one_codepoint", "add_utf16_bytes",
                   "add_utf32_bytes"]:
        print("errors:", errors)
        print("encode:", end=" ")
        try:
            print(codecs.encode("a\uDC80b\uDFFF", encoding, errors), end=" ")
        except UnicodeEncodeError as e:
            print(repr(e), end=" ")
        print()
        print("decode:", end=" ")
        try:
            print(codecs.decode(b'\x61\x80\x62\xFF', encoding, errors), end=" ")
        except UnicodeDecodeError as e:
            print(repr(e), end=" ")
        print()
        print()

test("ascii")
test("latin-1")
