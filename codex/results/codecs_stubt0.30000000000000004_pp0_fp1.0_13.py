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

def test_utf16_decode(encoding):
    # Test decoding UTF-16 with errors='surrogatepass'
    # This should not raise a UnicodeDecodeError, but a UnicodeTranslateError
    # instead.
    # Issue #11395
    with pytest.raises(UnicodeTranslateError):
        codecs.decode(b'\xff\xfe\xd8\x00', encoding, 'surrogatepass')

def test_utf32_decode(encoding):
    # Test decoding UTF-32 with errors='surrogatepass'
    # This should not raise a UnicodeDecodeError, but a UnicodeTranslateError
    # instead.
    # Issue #11395
    with pytest.raises(UnicodeTranslateError):
        codecs.decode(b'\xff\xfe\x00\x00\x00\x00', encoding, 'surrogatepass')

def test_utf16_encode(encoding):
    # Test encoding a surrogate character with errors='surrogatepass'
    # This should
