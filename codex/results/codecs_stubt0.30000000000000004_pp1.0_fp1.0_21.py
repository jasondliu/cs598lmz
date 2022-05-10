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
    # Test that the surrogatepass error handler works as expected.
    # The surrogatepass error handler is only available for UTF-16
    # and UTF-32.
    for encoding in ("utf-16", "utf-32"):
        for bad_bytes in (b'\x80', b'\x80\x80', b'\x80\x80\x80', b'\x80\x80\x80\x80'):
            for error_handler in ("strict", "surrogatepass", "ignore", "replace"):
                try:
                    bad_bytes.decode(encoding, error_handler)
                except UnicodeDecodeError as exc:
                    if error_handler == "surrogatepass":
                        assert exc.start == 0
                    else:
                        assert exc.start == 1
                else:
                    assert error_handler == "ignore"

    # Test that the surrogatepass error handler works as expected.
    # The surrogatepass error handler is only available for UTF-16
    # and UTF-32.
    for encoding in ("
