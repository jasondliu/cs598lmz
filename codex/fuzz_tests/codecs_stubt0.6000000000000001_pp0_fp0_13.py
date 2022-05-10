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

def test(encoding, s, error_handler):
    print("Encoding:", encoding)
    print("String:", s)
    print("Error:", error_handler)
    try:
        print("Encoded:", s.encode(encoding, error_handler))
    except Exception as e:
        print("Failed:", e)

test("utf-8", "abc", "strict")
test("utf-8", b"abc", "strict")
test("utf-8", "abc", "ignore")
test("utf-8", b"abc", "ignore")
test("utf-8", "abc", "replace")
test("utf-8", b"abc", "replace")
test("utf-8", "abc", "add_one_codepoint")
test("utf-8", b"abc", "add_one_codepoint")
test("utf-8", "abc", "add_utf16_bytes")
test("utf-8", b"abc", "add_utf16_bytes")
test("utf-8", "abc",
