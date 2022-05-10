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
    
def test_utf16_bom():
    """Check decoding UTF-16 with BOM mark and byteorder reversal."""
    big_endian_bytes = b'\xff\xfeA\x00\x00\x00'
    little_endian_bytes = big_endian_bytes[::-1]
    for text, src in [('A', big_endian_bytes),
                      ('A', little_endian_bytes),
                      ('\U0000000A', big_endian_bytes),
                      ('\U0000000A', little_endian_bytes)]:
        assert text.encode('utf-16') == src + b'\x00\x00'
        assert text.encode('utf-16-le')+b'\x00\x00' == src
        assert text.encode('utf-16-be')+b'\x00\x00' == src
        assert text.encode('utf-16-le') == src
        assert text.encode('utf-16-be') == src
        assert text.encode('utf
