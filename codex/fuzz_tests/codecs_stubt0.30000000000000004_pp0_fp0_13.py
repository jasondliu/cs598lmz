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

# Test that the error handler is called with the correct
# start and end arguments

def test_error_handler_args():
    def check(encoding, handler, input, expected):
        actual = input.decode(encoding, errors=handler)
        assert actual == expected
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        check(encoding, 'add_one_codepoint', b'\xff', 'a\ufffd')
        check(encoding, 'add_utf16_bytes', b'\xff', 'a\ufffd')
        check(encoding, 'add_utf32_bytes', b'\xff', 'a\ufffd')

# Test that the error handler is called with the correct
# start and end arguments

def test_error_handler_args():
    def check(encoding, handler, input, expected):
        actual = input.decode(encoding, errors=handler)
        assert actual == expected
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
       
