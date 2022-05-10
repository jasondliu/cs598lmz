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
    for enc in ("utf-8", "utf-8-sig"):
        for start in range(0, 0xd800):
            for end in range(start + 1, 0xd800):
                # Test UnicodeDecodeError
                try:
                    bytes(range(start, end)).decode(enc)
                except UnicodeDecodeError as exc:
                    assert exc.object == bytes(range(start, end))
                    assert exc.encoding == enc
                    assert exc.start == 0
                    assert exc.end == len(exc.object)
                    assert exc.reason == "invalid start byte"
                    assert exc.args == (enc, bytes(range(start, end)), 0, len(exc.object), "invalid start byte")

                # Test UnicodeEncodeError
                try:
                    chr(start).encode(enc, "add_one_codepoint")
                except UnicodeEncodeError as exc:
                    assert exc.object == chr(start)
                    assert exc.encoding == enc
                    assert
