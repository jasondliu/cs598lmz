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
    # Test UTF-16 and UTF-32 codecs
    for encoding in ("utf-16", "utf-32"):
        # Test decoding
        for error in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            # Test decoding with a BOM
            for bom in (b'\xff\xfe', b'\xfe\xff', b'\xff\xfe\x00\x00', b'\x00\x00\xfe\xff'):
                # Test decoding with a BOM and a partial codepoint at the end
                for partial in (b'', b'\x00', b'\x00\x00', b'\x00\x00\x00'):
                    # Test decoding with a BOM and a partial codepoint at the end
                    # and an error in the middle
                    for error_pos in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
