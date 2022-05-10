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

utf8_encoder = codecs.getencoder('utf_8')
utf16_encoder = codecs.getencoder('utf_16_le')
utf32_encoder = codecs.getencoder('utf_32_le')

def utf8_encode(unicode_string):
    return utf8_encoder(unicode_string, "add_one_codepoint")[0]

def utf16_encode(unicode_string):
    return utf16_encoder(unicode_string, "add_utf16_bytes")[0]

def utf32_encode(unicode_string):
    return utf32_encoder(unicode_string, "add_utf32_bytes")[0]

def utf16_decode(utf16_bytes):
    return codecs.getdecoder('utf_16_le')(utf16_bytes, 'ignore')[0]

def utf32_decode(utf32_bytes):
    return codecs.getdecoder('utf_32_
