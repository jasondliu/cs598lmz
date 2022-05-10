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

def test_decode(encoding):
    # test invalid byte sequence
    for i in range(len(bytes)):
        try:
            s = bytes[:i].decode(encoding)
        except UnicodeDecodeError:
            pass
        else:
            print(s)
            raise AssertionError("should have failed")

    # test decoding with replace error handler
    s = bytes.decode(encoding, "replace")
    assert s == "".join(["?"] * len(bytes))

    # test decoding with backslashreplace error handler
    s = bytes.decode(encoding, "backslashreplace")
    assert s == "".join(["\\x%02x" % x for x in bytes])

    # test decoding with xmlcharrefreplace error handler
    s = bytes.decode(encoding, "xmlcharrefreplace")
    assert s == "".join(["&#%d;" % x for x in bytes])

    # test decoding with add_one_codepoint error handler
    s = bytes.decode(encoding,
