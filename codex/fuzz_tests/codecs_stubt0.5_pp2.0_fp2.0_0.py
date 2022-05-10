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
    print(encoding)
    s = "abc"
    try:
        s.encode(encoding)
    except UnicodeEncodeError as exc:
        print(exc)
        print(exc.object)
        print(exc.start)
        print(exc.end)
        print(exc.reason)
        print(exc.object[exc.start:exc.end])
        print(exc.object.encode(encoding, "add_one_codepoint"))
        print(exc.object.encode(encoding, "add_utf16_bytes"))
        print(exc.object.encode(encoding, "add_utf32_bytes"))
        print()

test("ascii")
test("utf-8")
test("utf-16")
test("utf-32")
test("utf-16-le")
test("utf-32-le")
test("utf-16-be")
test("utf-32-be")
