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
    # Test codecs.register_error
    # Test that the error handler is called
    with captured_stdout() as stdout:
        b"abc\xff".decode("ascii", "add_one_codepoint")
    assert "add_one_codepoint" in stdout.getvalue()

    with captured_stdout() as stdout:
        b"ab\xff".decode("utf-16", "add_utf16_bytes")
    assert "add_utf16_bytes" in stdout.getvalue()

    with captured_stdout() as stdout:
        b"ab\xff".decode("utf-32", "add_utf32_bytes")
    assert "add_utf32_bytes" in stdout.getvalue()

    # Test that the error handler is not called
    with captured_stdout() as stdout:
        b"abc\xff".decode("ascii", "strict")
    assert "strict" not in stdout.getvalue()

    with captured_stdout() as std
