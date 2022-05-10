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

def test_main():
    # Test codecs.decode()
    #
    # codecs.decode(input, errors='strict')
    #
    # should raise a UnicodeDecodeError if the input string contains
    # characters not belonging to the target character set.

    # Test the 'strict' error handler
    for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
        for input, exp in (
            # invalid bytes
            (b'\x80', '\x80'),
            (b'\x80\x81', '\x80\x81'),
            (b'\x80\x81\x82', '\x80\x81\x82'),
            (b'\x80\x81\x82\x83', '\x80\x81\x82\x83'),
            (b'\x80\x81\x82\x83\x84', '\x80\x81\x82\x83\x84'),
            (
