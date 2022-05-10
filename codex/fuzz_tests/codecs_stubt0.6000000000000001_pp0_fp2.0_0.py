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
    # Default encoding
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        encoded_bytes = b'\xff'
        decoded_str = encoded_bytes.decode(encoding, errors='add_one_codepoint')
        expected_str = chr(0xff) + 'a'
        assert decoded_str == expected_str

    # UTF-16 with BOM
    encoded_bytes = b'\xff\xfe'
    decoded_str = encoded_bytes.decode('utf-16', errors='add_utf16_bytes')
    expected_str = '\uffffab'
    assert decoded_str == expected_str

    # UTF-16BE
    encoded_bytes = b'\xff\xfe'
    decoded_str = encoded_bytes.decode('utf-16-be', errors='add_utf16_bytes')
    expected_str = '\uffffab'
    assert decoded_str == expected_str

    # UTF-16LE
    encoded_
