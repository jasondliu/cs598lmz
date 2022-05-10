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

def test_main():
    # test utf-16-be
    for encoding in ("utf-16-be", "utf-16"):
        for i in range(0, 0xd800):
            s = chr(i).encode(encoding)
            assert s.decode(encoding, "strict") == chr(i)
            assert s.decode(encoding, "replace") == chr(i)
            assert s.decode(encoding, "ignore") == ""
            assert s.decode(encoding, "add_one_codepoint") == chr(i) + "a"
            assert s.decode(encoding, "add_utf16_bytes") == chr(i) + "a"
            assert s.decode(encoding, "add_utf32_bytes") == chr(i) + "a"

        for i in range(0xe000, 0x110000):
            s = chr(i).encode(encoding)
            assert s.decode(encoding, "strict") ==
