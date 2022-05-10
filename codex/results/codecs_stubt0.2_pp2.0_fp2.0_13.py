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
    # Test UTF-8
    for encoding in ("utf-8", "utf_8"):
        for i in range(0xD800, 0xE000):
            if i == 0xDFFF:
                continue
            # Test UTF-8 decoding
            s = bytes([i])
            try:
                s.decode(encoding)
            except UnicodeDecodeError as exc:
                assert exc.reason == "invalid continuation byte"
                assert exc.object is s
                assert exc.start == 0
                assert exc.end == 1
                assert exc.encoding == encoding
                assert exc.args == (s, 0, 1, "invalid continuation byte")
            else:
                assert False, "UnicodeDecodeError not raised"
            # Test UTF-8 encoding
            try:
                chr(i).encode(encoding)
            except UnicodeEncodeError as exc:
                assert exc.reason == "invalid continuation byte"
                assert exc.object is s
                assert exc.start == 0
                assert exc.
