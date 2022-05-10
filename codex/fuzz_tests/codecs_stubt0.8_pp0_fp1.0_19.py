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

def test_utf32_decode_error():
    "Decoding UTF-32 bytes with replace or backslashreplace"
    # example: "\xa8@\xa8" is a 2-byte character in shift_jis (with 0x5c
    # as lead byte).
    bytes = b"\xa8@\xa8@\xa8\x00\xa8\x00\xa8\x80\xa8\x80\xa8\xbf\xa8\xbf"
    for decoder in ("utf-32", "utf-32-be", "utf-32-le"):
        for final in (True, False):

            # Replace error handler
            decoded = bytes.decode(decoder, "replace")
            assert decoded.count("?") == 6
            assert len(decoded) - decoded.count("?") == 3  # 3 half-characters

            # Backslashreplace error handler
            decoded = bytes.decode(decoder, "backslashreplace")
            assert decoded.count("?") == 0
           
