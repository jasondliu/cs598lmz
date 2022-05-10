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
    # Make sure that the error handler is called with the correct
    # start index.

    # UCS-2
    for encoding in ("utf-16", "utf-16-le", "utf-16-be"):
        s = b'\xff'
        decoded, consumed = codecs.utf_16_decode(s, "replace", encoding)
        assert consumed == 2
        assert decoded == '\ufffd'

        s = b'\xff\xfe'
        decoded, consumed = codecs.utf_16_decode(s, "replace", encoding)
        assert consumed == 2
        assert decoded == '\ufffd'

        s = b'\xff\xfe\xff'
        decoded, consumed = codecs.utf_16_decode(s, "replace", encoding)
        assert consumed == 2
        assert decoded == '\ufffd'

        s = b'\xff\xfe\xff\xfe'
        decoded, consumed = codecs.utf_16_decode(s, "replace",
