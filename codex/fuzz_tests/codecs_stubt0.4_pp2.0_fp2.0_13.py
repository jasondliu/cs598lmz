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
    # This test checks whether the error handlers are called with the right
    # arguments.  It doesn't check whether the error handlers do the right
    # thing.
    s = "abc"
    u = "abc"

    # Test the default error handler
    try:
        s.encode("ascii", "strict")
    except UnicodeEncodeError as exc:
        if exc.object is not s:
            raise TestFailed("wrong exception object")
        if exc.encoding != "ascii":
            raise TestFailed("wrong encoding")
        if exc.start != 3:
            raise TestFailed("wrong start")
        if exc.end != 3:
            raise TestFailed("wrong end")
        if exc.reason != "ordinal not in range(128)":
            raise TestFailed("wrong reason")
        if exc.object[exc.start:exc.end] != "":
            raise TestFailed("wrong object")
    else:
        raise TestFailed("didn't raise UnicodeEncodeError")

    # Test
