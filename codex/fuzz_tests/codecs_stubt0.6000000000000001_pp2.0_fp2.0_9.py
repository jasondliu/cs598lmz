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
    # Testing UTF-8
    for encoding in ("utf_8", "utf-8"):
        s = "\ud800"
        try:
            s.encode(encoding)
        except UnicodeEncodeError as e:
            s = s.encode(encoding, "add_one_codepoint")
            assert s == "a".encode(encoding), s
        s = "\udc00"
        try:
            s.encode(encoding)
        except UnicodeEncodeError as e:
            s = s.encode(encoding, "add_one_codepoint")
            assert s == "a".encode(encoding), s
        s = "\ud800\udc00"
        try:
            s.encode(encoding)
        except UnicodeEncodeError as e:
            s = s.encode(encoding, "add_one_codepoint")
            assert s == "a".encode(encoding), s

    # Testing UTF-16
    for encoding in ("utf_16
