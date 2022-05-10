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
    def try_encode(encoding, errors, input, expected_output, expected_exc = None):
        try:
            result = codecs.encode(input, encoding, errors)
            assert result == expected_output
            assert expected_exc is not None
        except expected_exc:
            pass

    # Test that we can decode a surrogate pair in UTF-16.
    try_encode("utf-16", None, "\U00023456", b'\x34\x12\x56\x34')
    try_encode("utf-16-le", None, "\U00023456", b'\x34\x12\x56\x34')
    try_encode("utf-16-be", None, "\U00023456", b'\x12\x34\x34\x56')

    # Test that we can decode a surrogate pair in UTF-32.
    try_encode("utf-32", None, "\U00023456", b'\x00\x00\x23\x34\x00\x
