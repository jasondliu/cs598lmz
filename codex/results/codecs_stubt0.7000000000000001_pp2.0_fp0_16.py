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
    test_utf7()
    test_utf8()
    if sys.maxunicode >= 0x10000:
        test_utf16()
        test_utf32()
    test_ascii()
    test_iso8859()
    test_mbcs()
    test_issue6059()

def test_iso8859():
    for i in range(1, 16):
        # Encode
        s = list(range(32)) + [i*16 + j for j in range(16)]
        s = bytes(s)
        t = s.decode("iso8859-%d" % i, "replace")
        u = t.encode("iso8859-%d" % i, "replace")
        if s != u:
            raise TestFailed("encode/decode iso8859-%d" % i)

        # Roundtrip
        s = list(range(32)) + [i*16 + j for j in range(16)]
        s = bytes(s)
        t = s.decode("
