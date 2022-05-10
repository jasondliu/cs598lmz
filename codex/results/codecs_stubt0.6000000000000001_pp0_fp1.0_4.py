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

# These are to be re-used in all tests

# This is the string we will be encoding.
# It contains a character that is not allowed in the target encoding
exception_string = "a\u20acb"

# This is the expected string after encoding
encoded_string = b"a\xe2\x82\xacb"

# This is the expected string after encoding, after we replace the bad character
# with the replacement character, U+FFFD
encoded_string_with_replacement = b"a\xef\xbf\xbd\xe2\x82\xacb"

# This is the expected string after encoding, after we replace the bad character
# with the replacement character, U+FFFD, and then we decode the result
# with UTF-16 or UTF-32
encoded_string_with_replacement_decoded = "a\ufffdb"

# This is the expected string after encoding, after we replace the bad character
# with the replacement character, U+FFFD, and then we decode the result
# with UTF-16 or UTF-
