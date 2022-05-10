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
    # test UTF-8
    for errorhandler in (None, "strict", "ignore", "replace", "add_one_codepoint"):
        for start in range(0, len(utf8_bytes)):
            for end in range(start, len(utf8_bytes)):
                b = utf8_bytes[start:end]
                if errorhandler is None:
                    try:
                        u = b.decode("utf-8")
                    except UnicodeDecodeError:
                        pass
                    else:
                        assert u == utf8_text
                else:
                    u = b.decode("utf-8", errorhandler)
                    assert u == utf8_text

    # test UTF-16
    for errorhandler in (None, "strict", "ignore", "replace", "add_utf16_bytes"):
        for start in range(0, len(utf16_bytes)):
            for end in range(start, len(utf16_bytes)):
                b = utf16_bytes[start:end]

