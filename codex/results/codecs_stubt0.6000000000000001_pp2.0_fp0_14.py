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
    print("testing UTF-16 decoder...")
    utf16_decoder = codecs.getdecoder("utf-16")

    def decode(input, errors="strict"):
        return utf16_decoder(input, errors)[0]

    # test the error handler
    assert decode(b'\xff\xfe\x00\x00', "add_one_codepoint") == "\u0000\ufffd"
    assert decode(b'\xff\xfe\x00', "add_one_codepoint") == "\u0000\ufffd"
    assert decode(b'\xff\xfe', "add_one_codepoint") == "\u0000\ufffd"
    assert decode(b'\xff\xfe\x00\x00', "add_utf16_bytes") == "\u0000\u00ab"
    assert decode(b'\xff\xfe\x00', "add_utf16_bytes") == "\u0000\u00ab"
    assert decode(b'\xff\xfe
