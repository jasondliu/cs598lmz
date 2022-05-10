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


# Test cases are taken from
# https://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-test.txt
# Some of the tests are commented out because they don't work as intended.

def test_bad_utf8(b, replacement=b'?'):
    # given the starting byte of an invalid UTF-8 codepoint,
    # check that the UTF-8 decoder consumes one character
    # and that it replaces the byte sequence with a replacement
    # character.

    # check the replacement byte first
    assert codecs.utf_8_decode(b'\x00'*b + replacement + b'\x00', "strict", False) == (
        b'\x00'*b + replacement + b'\x00',
        b+1
    )

    # same test with an "add_one_codepoint" error handler
    # in this case, the replacement character itself is replaced
    assert codecs.utf_8_decode(b'\x00'*b + replacement + b'\
