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

# The following test is based on the test_codecs.py test_surrogates,
# but it tests the surrogatepass error handler.

# The surrogatepass error handler is only available in Python 3.3 and later.
if sys.version_info >= (3, 3):
    def check_surrogatepass(encoding, data):
        for errors in ('surrogatepass', 'surrogateescape'):
            # Encode
            encoded = data.encode(encoding, errors)
            # Decode
            decoded = encoded.decode(encoding, errors)
            # Check that the decoded data is the same as the original
            if decoded != data:
                raise ValueError("decoded data is different from the original")
            # Check that the encoded data is the same as the original
            if encoded != data.encode(encoding):
                raise ValueError("encoded data is different from the original")

    # Test with a single surrogate
    check_surrogatepass('utf-16', '\ud800')
    check_surrogatepass('utf-
