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

# This test is written in such a way that the UTF-8 codec should be able
# to decode the entire input string without error.  If the UTF-8 codec
# is not able to decode the entire input string without error, the test
# fails.

# The UTF-8 codec should be able to decode the entire input string
# without error.

# The UTF-16 codec should be able to decode the entire input string
# with error.  The error handler should be called once for each
# invalid byte sequence in the input string.  The error handler should
# replace each invalid byte sequence with a single U+FFFD character.
# The UTF-16 codec should return a string that contains the same
# number of characters as the input string.

# The UTF-32 codec should be able to decode the entire input string
# with error.  The error handler should be called once for each
# invalid byte sequence in the input string.  The error handler should
# replace each invalid byte sequence with a single U+FFFD character.
# The UTF-32 codec should return a string that contains the same
# number of characters as the input string
