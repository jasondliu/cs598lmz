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
    test_unicode_internal_encode()
    test_unicode_internal_decode()
    test_unicode_encode_decode()
    test_unicode_escape_decode()
    test_raw_unicode_escape_decode()
    test_unicode_escape_encode()
    test_raw_unicode_escape_encode()
    test_unicode_internal_decode_error()
    test_unicode_decode_error()
    test_unicode_encode_error()
    test_unicode_escape_decode_error()
    test_unicode_escape_encode_error()
    test_raw_unicode_escape_decode_error()
    test_raw_unicode_escape_encode_error()
    test_utf7()
    test_utf8()
    test_utf16()
    test_utf32()
    test_unicode_charmap_encode()
    test_unicode_charmap_decode()
    test_unic
