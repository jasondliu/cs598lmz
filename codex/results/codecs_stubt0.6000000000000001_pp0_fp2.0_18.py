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

def test(encoding, errors=None):
    s = "abcdefg"
    b = s.encode(encoding)
    if errors:
        b = b[:3] + b'\x00\x00\x00\x00' + b[-2:]
    s2 = b.decode(encoding, errors)
    print(s2)
    if s2 != s:
        print("FAILED:", errors)
        raise AssertionError

print("Test 1")
test("utf-8")
test("utf-8", "add_one_codepoint")
test("utf-8", "add_utf16_bytes")
test("utf-8", "add_utf32_bytes")

print("Test 2")
test("utf-16")
test("utf-16", "add_one_codepoint")
test("utf-16", "add_utf16_bytes")
test("utf-16", "add_utf32_bytes")

print("Test 3")
test("utf-32")
test("utf
