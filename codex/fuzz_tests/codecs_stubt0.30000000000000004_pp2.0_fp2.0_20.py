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
    # Test that the error handlers are called with the correct exception
    # object.
    for encoding in ["utf-8", "utf-16", "utf-32"]:
        for errors in ["strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"]:
            for input in ["\x80", "\x80\x80", "\x80\x80\x80", "\x80\x80\x80\x80"]:
                try:
                    codecs.decode(input.encode(encoding), encoding, errors)
                except UnicodeDecodeError as exc:
                    if errors == "strict":
                        pass
                    elif errors == "replace":
                        assert exc.object == input.encode(encoding)
                        assert exc.start == 0
                        assert exc.end == len(input.encode(encoding))
                        assert exc.reason == "unknown"
                        assert exc.encoding == encoding
                    elif errors == "ignore":

