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

# This is a list of (input_bytes, encoding, expected_output, error_handler) tuples.
# The expected output is a list of (decoded_text, length_of_input_bytes_consumed)
# tuples.
TEST_CASES = [
    (b'\xff', 'latin-1', [(u'\ufffd', 1)]),
    (b'\xff', 'ascii', [(u'\ufffd', 1)]),
    (b'\xff', 'utf-8', [(u'\ufffd', 1)]),
    (b'\xff', 'utf-16', [(u'\ufffd', 2)]),
    (b'\xff', 'utf-32', [(u'\ufffd', 4)]),

    (b'\xff\xfe', 'utf-16', [(u'\ufffd', 2)]),
    (b'\xff\xfe', 'utf-16-le', [(u'\ufffd', 2)]),
    (b'\xff\xfe', 'utf-16-be', [(
