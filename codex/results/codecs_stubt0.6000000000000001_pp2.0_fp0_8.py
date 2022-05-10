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
    test_sizes()
    test_bad_decode_args()
    test_decode_unicode()
    test_decode_unicode_escape()
    test_decode_raw_unicode_escape()
    test_decode_latin_1()
    test_decode_utf8()
    test_decode_utf8_surrogatepass()
    test_decode_utf8_surrogatedecode()
    test_decode_utf8_decodeerror()
    test_decode_utf16()
    test_decode_utf16_be()
    test_decode_utf16_le()
    test_decode_utf16_be_surrogatepass()
    test_decode_utf16_le_surrogatepass()
    test_decode_utf16_be_surrogatedecode()
    test_decode_utf16_le_surrogatedecode()
    test_decode_utf16_be_decodeerror()
    test_decode_
