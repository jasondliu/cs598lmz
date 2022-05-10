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

encoding_2_byte = 'utf16'
encoding_3_byte = 'utf32'

encoding_2_byte_LE = encoding_2_byte + '-le'
encoding_2_byte_BE = encoding_2_byte + '-be'
encoding_3_byte_LE = encoding_3_byte + '-le'
encoding_3_byte_BE = encoding_3_byte + '-be'

encodings_2_byte = [ encoding_2_byte_LE, encoding_2_byte_BE ]
encodings_3_byte = [ encoding_3_byte_LE, encoding_3_byte_BE ]

codecs_4_byte = [ 'utf-32', 'utf-32-be' ]
unicode_max_LE = sys.maxunicode
unicode_max_BE = sys.maxunicode

# mapping from bytes to unicode
test_unicode_mapping = {
        b'\x00\x00'          : b'\x00\x00'.decode(encoding
