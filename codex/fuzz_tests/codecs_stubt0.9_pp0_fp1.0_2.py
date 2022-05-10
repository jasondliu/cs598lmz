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

def test_readfunc(codecname, encoding, test_decodes, test_decodes_raw):
    def readfunc(b):
        length = len(b)
        return (b"",length)
    if test_decodes:
        if encoding.startswith("utf-16"):
            codec = codecs.getincrementaldecoder(codecname)
            f = codec(encoding, "replace")
            assert decode_test(f, b"a\xc0\x00\x80\x00\x80", add_utf16_bytes) == \
                         ("a\ufffd\x00\udc80\x00\udc80", b"")
        else:
            codec = codecs.getincrementaldecoder(codecname)
            f = codec(encoding, "replace")
            assert decode_test(f, b"a\x80\xc0", add_one_codepoint) == \
                         ('a\ufffd\ufffd', b"")

    if test_decodes_raw:
        if
