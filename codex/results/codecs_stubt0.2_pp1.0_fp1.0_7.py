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
    # Test UnicodeEncodeError
    for encoding in ["ascii", "utf-8", "utf-16", "utf-32"]:
        for errors in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
            try:
                u"\U0010ffff".encode(encoding, errors)
            except UnicodeEncodeError as exc:
                assert exc.object == u"\U0010ffff"
                assert exc.encoding == encoding
                assert exc.start == 0
                assert exc.end == 1
                assert exc.reason == "illegal Unicode character"
                assert exc.args == (u"\U0010ffff", 0, 1, "illegal Unicode character")
            else:
                assert encoding == "utf-8" and errors == "ignore"

    # Test UnicodeDecodeError
    for encoding in ["ascii", "utf-8", "utf-16", "utf-32"]:
        for errors in ["strict", "replace", "
