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

def test_utf8_decode_error_handling():
    # Test UTF-8 decoding with various error handling schemes
    for s in ["\xff", "\xff\xff", "\xff\xff\xff", "\xff\xff\xff\xff"]:
        for error_handler in (None, "strict", "ignore", "replace", "add_one_codepoint"):
            try:
                s.decode("utf-8", error_handler)
            except UnicodeDecodeError:
                if error_handler is None:
                    pass
                else:
                    raise

def test_utf16_decode_error_handling():
    # Test UTF-16 decoding with various error handling schemes
    for s in [b"\xff", b"\xff\xff", b"\xff\xff\xff", b"\xff\xff\xff\xff"]:
        for error_handler in (None, "strict", "ignore", "replace", "add_utf16_bytes"):
            try:
                s.decode("utf-16", error_handler)
            except
