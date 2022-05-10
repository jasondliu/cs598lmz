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
    for enc in ("utf-8", "utf_8"):
        for i in range(0, 0x110000, 0x100):
            s = chr(i)
            try:
                s.encode(enc)
            except UnicodeEncodeError:
                pass
            else:
                raise AssertionError("%s should not encode U+%04X" % (enc, i))

        for i in range(0, 0x110000, 0x100):
            s = chr(i)
            try:
                s.encode(enc, "add_one_codepoint")
            except UnicodeEncodeError:
                raise AssertionError("%s should encode U+%04X" % (enc, i))

        for i in range(0, 0x110000, 0x100):
            s = chr(i)
            try:
                s.encode(enc, "add_utf16_bytes")
            except UnicodeEncodeError:
                raise AssertionError("
