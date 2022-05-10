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

def test_codec_utf8(encoding_mod):
    INVALID_UTF8_INPUT = b"\xf3\x28\x8c\xbc"
    # U+2F804: CJK UNIFIED IDEOGRAPH-2F804
    VALID_UTF8_INPUT = b"\xf0\xaf\xa0\x84"
    # U+110000: not a Unicode code point
    INVALID_UNICODE_INPUT = "\U00110000"

    # Encoding
    assert codecs.lookup(encoding_mod.__name__).name == encoding_mod.__name__
    assert encoding_mod.encode(INVALID_UTF8_INPUT) ==  (INVALID_UTF8_INPUT, len(INVALID_UTF8_INPUT))
    assert encoding_mod.encode(VALID_UTF8_INPUT) == (VALID_UTF8_INPUT, len(VALID_UTF8_INPUT))

    # Decoding
    # Default strict mode: raise Unicode
