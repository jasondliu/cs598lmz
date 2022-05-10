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
    for encoding in ("utf-16", "utf-16-le", "utf-16-be", "utf-32", "utf-32-le", "utf-32-be"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            for i in range(0, len(utf8_bytes)):
                for j in range(i, len(utf8_bytes)):
                    utf8_chunk = utf8_bytes[i:j]
                    utf8_chunk_decoded = utf8_chunk.decode("utf-8")

                    # Encode
                    encoded = utf8_chunk.decode(encoding, errors)
                    if errors == "strict":
                        assert encoded == utf8_chunk_decoded
                    elif errors == "replace":
                        assert encoded == utf8_chunk_decoded.
