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
    # test codecs.register_error()
    #
    # test that the error handler is called with the correct exception
    # and that the correct replacement is returned
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            if errors == "add_one_codepoint":
                expected = b"a\xff"
            elif errors == "add_utf16_bytes":
                expected = b"ab\xff"
            elif errors == "add_utf32_bytes":
                expected = b"abcd\xff"
            else:
                expected = b"\xff"
            s = codecs.decode(b"\xff", encoding, errors)
            if s != expected:
                raise TestFailed("decoding %r with %r failed" % (b"\xff", errors))
            s = codecs.encode
