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
    # Test unicode-escape
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            for input in (b"\\u1234", b"\\U00012345", b"\\U00012345\\u1234"):
                try:
                    res = codecs.unicode_escape_decode(input, errors)[0]
                except UnicodeDecodeError as e:
                    res = e.object
                if errors == "strict":
                    assert res == input
                elif errors == "replace":
                    assert res == b"?"
                elif errors == "ignore":
                    assert res == b""
                elif errors == "add_one_codepoint":
                    assert res == b"a"
                elif errors == "add_utf16_bytes":
                    assert res == b"ab"
                elif errors == "
