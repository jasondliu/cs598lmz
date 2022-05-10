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
    print("%s with %s" % (encoding, errors))
    try:
        codecs.decode(b"\xff", encoding, errors)
    except UnicodeDecodeError as exc:
        print(exc)
        print(codecs.decode(b"\xff", encoding, errors))
    print()

test("ascii", "strict")
test("ascii", "ignore")
test("ascii", "replace")
test("ascii", "add_one_codepoint")
test("ascii", "add_utf16_bytes")
test("ascii", "add_utf32_bytes")

test("utf-8", "strict")
test("utf-8", "ignore")
test("utf-8", "replace")
test("utf-8", "add_one_codepoint")
test("utf-8", "add_utf16_bytes")
test("utf-8", "add_utf32_bytes")

test("utf-16", "strict
