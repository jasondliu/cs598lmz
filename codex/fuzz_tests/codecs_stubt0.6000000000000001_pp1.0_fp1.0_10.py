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
    for encoding in ["utf-8", "utf-16", "utf-32"]:
        try:
            codec = codecs.lookup(encoding)
        except LookupError:
            continue
        # Encode a string with an error handler that adds one code point.
        # This results in a single replacement character.
        encoded = codec.encode("\x80", "add_one_codepoint")
        # Now try to decode this string with a surrogate pass handler.
        # This should result in a single replacement character.
        decoded = codec.decode(encoded, "surrogatepass")
        assert decoded == u"\ufffd", (encoding, decoded)

        if encoding == "utf-8":
            # Encode a string with an error handler that adds one code point.
            # This results in a single replacement character.
            encoded = codec.encode("\x80", "add_one_codepoint")
            # Now try to decode this string with a strict handler.
            # This should result in a UnicodeDecode
