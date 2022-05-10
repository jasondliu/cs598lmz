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
    def assertEqual(a, b):
        if a != b:
            raise AssertionError(a, b)

    # test the codecs.escape_encode/decode helper functions
    assertEqual(codecs.escape_decode(b"a\\x61c"), (b"aac", 2))
    assertEqual(codecs.escape_decode(b"\\x61\\x62\\x63"), (b"abc", 6))
    assertEqual(codecs.escape_decode(b"\\x61\\x62\\x63\\x61b"), (b"abcab", 8))
    assertEqual(codecs.escape_decode(b"\\U00010001"), (b"\xf0\x90\x80\x81", 10))
    assertEqual(codecs.escape_decode(b"\\U00010001\\U00010002"), (b"\xf0\x90\x80\x81\xf0\x90\x80\x82", 20))

