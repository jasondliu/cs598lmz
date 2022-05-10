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
    print(encoding, "start")
    try:
        s = b'\xd8\x00'
        u = s.decode(encoding)
    except UnicodeDecodeError as exc:
        u = s.decode(encoding, "add_one_codepoint")
        assert u == 'a\ud800', repr(u)
    else:
        raise Exception("did not raise UnicodeDecodeError")
    print(encoding, "end")
    print()

test("utf-16")
test("utf-16-le")
test("utf-16-be")
test("utf-32")
test("utf-32-le")
test("utf-32-be")
