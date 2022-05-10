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

# The following tests test that the decoder doesn't raise UnicodeDecodeError
# when an invalid byte sequence is encountered. Instead, the codec_error
# handler is called.

# Unicode data
#
# Note: Some of the following tests are commented out because the invalid bytes
# are not valid in any encoding. For example, the UTF-16 encoder cannot encode
# 0x12345678 into two bytes, because 0x1234 is not a valid UTF-16 surrogate
# value.
#
# Note: Just like it's possible to add a byte by the codec_error handler, it's
# also possible to remove a byte from the input buffer. This is done by
# returning an empty string from the handler.

decoding_table = [
    # Unicode escapes
    (b'\\u1234', "a", "utf-8", "add_one_codepoint"),
    (b'\\U00012345', "a", "utf-8", "add_one_codepoint"),

    # UTF-8
    (b'\xc2', "a", "utf-8", "add
