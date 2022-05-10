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
    for i in range(0xD800, 0xE000):
        # Test invalid UTF-8
        try:
            codecs.utf_8_decode(chr(i).encode("utf-8"), "strict")
        except UnicodeDecodeError as exc:
            if exc.object != chr(i).encode("utf-8") or exc.start != 0 or \
               exc.end != 1 or exc.reason != "invalid start byte":
                raise
        else:
            raise AssertionError("UnicodeDecodeError not raised")
        # Test invalid UTF-8 with add_one_codepoint
        try:
            codecs.utf_8_decode(chr(i).encode("utf-8"), "add_one_codepoint")
        except UnicodeDecodeError as exc:
            if exc.object != chr(i).encode("utf-8") or exc.start != 0 or \
               exc.end != 1 or exc.reason != "invalid
