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

def utf_16_exception_decoder(input, errors='strict'):
    output = codecs.utf_16_le_decode(input, errors, 0)
    if isinstance(output[0], str):
        output = 'exception'
    return (output, len(input))

def utf_8_exception_encoder(input, errors='strict'):
    output = codecs.utf_8_encode(input, errors)
    if isinstance(output[0], bytes):
        output = b'exception'
    return (output, len(input))


### Cursor movement commands ### {{{1
keyword(r"\A(?P<action>h|l|\^|0|M$|L$|\$|H|M|G|%|[fF]|t|T|j|k|[+-]|[\d]+[kKlLhHwW]|[\d]+(|\.[\d]+)[Gg])")
# k th, l th, ^
