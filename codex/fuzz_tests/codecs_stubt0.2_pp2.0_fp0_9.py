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
    # Test UTF-16
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        # Test decoding
        for error_handler in ("strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes"):
            for input in (b"\xff", b"\xff\xff", b"\xff\xff\xff", b"\xff\xff\xff\xff"):
                try:
                    codecs.decode(input, encoding, error_handler)
                except UnicodeDecodeError as exc:
                    if error_handler == "strict":
                        pass
                    elif error_handler == "ignore":
                        assert exc.object == input
                        assert exc.start == 0
                        assert exc.end == len(input)
                        assert exc.reason == "invalid continuation byte"
                    elif error_handler == "replace":
                        assert exc.object == input
                        assert exc.start == 0
                        assert exc.end == len(input)
                        assert exc
