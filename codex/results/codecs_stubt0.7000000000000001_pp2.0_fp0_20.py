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
    utf16_encoding = 'utf16'
    utf32_encoding = 'utf32'

    # Get the UTF-8 representation of the surrogate pair
    surrogate_pair = b'\xed\xa0\x80\xed\xb0\x80'

    # Get the UTF-8 representation of the UTF-16 and UTF-32 BOMs
    utf16_bom = codecs.BOM_UTF16
    utf32_bom = codecs.BOM_UTF32

    # Get the UTF-8 representation of the U+10FFFF character
    u10ffff = b'\xf4\x8f\xbf\xbf'

    # Get the UTF-8 representation of the U+110000 character (invalid)
    invalid_codepoint = b'\xf4\x90\x80\x80'


    # check UTF-16 BOM handling
    for boms in ((b'', utf16_bom), (utf16_bom, utf16_bom)):
        for
