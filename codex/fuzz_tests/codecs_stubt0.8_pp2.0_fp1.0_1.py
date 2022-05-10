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
    assert "abcdabcd" == u"abcd".encode("utf-16", "add_one_codepoint")
    assert "abcdabcdabcdab" == u"abcd".encode("utf-32", "add_one_codepoint")
    assert b"abcdabcd" == b"abcd".decode("utf-16", "add_utf16_bytes")
    assert b"abcdabcdabcdab" == b"abcd".decode("utf-32", "add_utf32_bytes")

if __name__ == "__main__":
    test_main()
