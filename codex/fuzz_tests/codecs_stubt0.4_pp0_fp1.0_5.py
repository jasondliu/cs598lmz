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
    test_unicode_escape_encode_decode()
    test_raw_unicode_escape_encode_decode()
    test_latin1_encode_decode()
    test_ascii_encode_decode()
    test_utf7_encode_decode()
    test_utf8_encode_decode()
    test_utf16_encode_decode()
    test_utf16_le_encode_decode()
    test_utf16_be_encode_decode()
    test_utf32_encode_decode()
    test_utf32_le_encode_decode()
    test_utf32_be_encode_decode()
    test_unicode_internal_encode_error()
    test_unicode_internal_decode_error()
    test_unicode_encode_error
