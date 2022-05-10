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
    import sys
    if sys.platform == 'win32':
        # This test doesn't make sense on Windows, since the
        # surrogatepass error handler is not available
        return

    # test surrogatepass
    for encoding in ["utf-16", "utf-32"]:
        for errors in ["surrogatepass", "surrogateescape"]:
            for input in ["\ud800", "\udc00", "\ud800\ud800", "\udc00\udc00",
                          "\ud800\udc00", "\udc00\ud800"]:
                for i in range(len(input)):
                    got = input[:i].encode(encoding, errors)
                    expect = input[:i].encode(encoding, "strict")
                    assert got == expect, (encoding, errors, input, i, got, expect)

    # test other error handlers
    for encoding in ["utf-16", "utf-32"]:
        for errors in ["add_one_codepoint", "add_utf16_bytes", "
