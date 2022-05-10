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

CCK = codecs.lookup_error("add_one_codepoint")
CU16B = codecs.lookup_error("add_utf16_bytes")
CU32B = codecs.lookup_error("add_utf32_bytes")
CU16BE = codecs.lookup_error("add_utf16_bytes")
CU16LE = codecs.lookup_error("add_utf16_bytes")
CU32BE = codecs.lookup_error("add_utf32_bytes")
CU32LE = codecs.lookup_error("add_utf32_bytes")
CP1252 = codecs.lookup_error("replace")

def encode_add_one(input, errors="strict"):
    if errors=="add_one_codepoint":
        return codecs.charmap_encode(input, errors, encoding_table)[0]
    return codecs.utf_8_encode(input, errors)[0]

def decode_add_one(input, errors="strict"):
    if errors=="add_one
