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

# Test the 'surrogateescape' error handler

# This is a list of (input, output) tuples.
# The input is a byte string that is not valid UTF-8.
# The output is the expected result from the 'surrogateescape' error handler.
# The output is a list of (string, start, end) tuples.
# The string is the decoded string, start and end are the start and end
# indices of the input byte string that were decoded to produce the output
# string.
#
# The test data is taken from the Python 3.2 test suite.

test_data = [
    (b'\x80', [('\udc80', 0, 1)]),
    (b'\x80\x81', [('\udc80', 0, 1), ('\udc81', 1, 2)]),
    (b'\xc3\x80', [('\u00c3', 0, 2)]),
    (b'\xc3\x80\xc3\x81', [('\u00c3', 0, 2),
