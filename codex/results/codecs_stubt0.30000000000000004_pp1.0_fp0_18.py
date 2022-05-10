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
        for error in ("strict", "ignore", "replace", "add_one_codepoint",
                      "add_utf16_bytes", "add_utf32_bytes"):
            if encoding == "utf-16":
                # Test decoding with a BOM
                for bom in (b'', b'\xff\xfe', b'\xfe\xff'):
                    for data in (b'\x00\x00', b'\x00\x00\x00\x00'):
                        for i in range(0, len(data), 2):
                            for j in range(i, len(data), 2):
                                for k in range(j, len(data), 2):
                                    s = bom + data[:i] + data[j:k]
                                    if error == "strict":
                                        raises(UnicodeDecodeError, s.decode,
                
