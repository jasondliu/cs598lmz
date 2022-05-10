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

utf8_handler = codecs.lookup('utf-8')
utf16_handler = codecs.lookup('utf-16')
utf32_handler = codecs.lookup('utf-32')

utf8_encode = utf8_handler.encode
utf16_encode = utf16_handler.encode
utf32_encode = utf32_handler.encode
utf8_decode = utf8_handler.decode
utf16_decode = utf16_handler.decode
utf32_decode = utf32_handler.decode

# The test vectors are copied from ICU4C tests/conversion
# (see ICU4C_SRC/icu4c/source/test/intltest/convrin.unicode)

# str, bytes, str, bytes
simple_bmp_test_vectors = (
    (('a', 'ab\\u0100', '\u0100'),
                     b'a\x00a\x00\xc0\x80\x00\x00',
                     '
