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
    # test unicode encode error handler
    for errors in ["strict", "ignore", "replace", "add_one_codepoint"]:
        for encoding in ["utf-8", "ascii", "utf-16-le"]:
            if errors == "add_one_codepoint" and encoding != "utf-16-le":
                continue
            for u in ["", "\u3042", "\u3042\u3042", "\u3042\u3044"]:
                try:
                    b = u.encode(encoding, errors)
                except UnicodeEncodeError as e:
                    if errors == "strict":
                        pass
                    elif errors == "ignore":
                        assert b == b""
                    elif errors == "replace":
                        assert b == b"?"
                    elif errors == "add_one_codepoint":
                        assert b == b"a"
                    else:
                        raise
                else:
                    if errors == "strict":
                        assert b == u.encode(encoding)
                    el
