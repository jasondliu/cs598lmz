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
    print("testing", encoding)
    try:
        u = chr(0xdc00)
        u.encode(encoding)
    except UnicodeEncodeError as exc:
        print("UnicodeEncodeError:", exc.reason, exc.object[exc.start:exc.end])
        print("add_one_codepoint:", exc.object.encode(encoding, "add_one_codepoint"))
        print("add_utf16_bytes:", exc.object.encode(encoding, "add_utf16_bytes"))
        print("add_utf32_bytes:", exc.object.encode(encoding, "add_utf32_bytes"))
    else:
        print("no error")

test("utf-16-le")
test("utf-16-be")
test("utf-32-le")
test("utf-32-be")
