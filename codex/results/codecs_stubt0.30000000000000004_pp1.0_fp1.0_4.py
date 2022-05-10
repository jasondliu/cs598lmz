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

encoding_map = {
    "utf-8": "utf_8",
    "utf-16": "utf_16",
    "utf-32": "utf_32",
    "utf-16-be": "utf_16_be",
    "utf-16-le": "utf_16_le",
    "utf-32-be": "utf_32_be",
    "utf-32-le": "utf_32_le",
}

def test_decode_error_handling():
    for encoding in encoding_map:
        # Test the default error handling
        with pytest.raises(UnicodeDecodeError):
            codecs.decode(b'\xff', encoding)

        # Test the 'strict' error handling
        with pytest.raises(UnicodeDecodeError):
            codecs.decode(b'\xff', encoding, 'strict')

        # Test the 'replace' error handling
        assert codecs.decode(b'\xff', encoding, 'replace') == u'\ufffd'

       
