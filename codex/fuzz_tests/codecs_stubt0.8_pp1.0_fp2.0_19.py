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

# The test string is the '\u8c00' UTF-8 encoded; if you would
# decode it to UCS-4, it would be the '\ud800\udc00' surrogate
# pair that cannot be converted to UTF-16.
test_string = b'\xed\xa0\x80'

def test_add_one_codepoint(input_bytes, encoding,
                           test_string=test_string):
    assert input_bytes == test_string
    try:
        decode(input_bytes, encoding, "strict")
    except UnicodeDecodeError:
        raise unittest.SkipTest("Need UTF-32 codec")

    decoded = decode(input_bytes, encoding, "add_one_codepoint")
    assert decoded == '\udc00a'
    decoded_bytes = encode(decoded, encoding, "strict")
    assert decoded_bytes == test_string


def test_add_utf16_bytes(input_bytes, encoding,
                         test_string=test_string):
    assert input_bytes
