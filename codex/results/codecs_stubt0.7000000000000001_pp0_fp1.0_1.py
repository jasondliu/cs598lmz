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

    # Test handling of different kinds of errors
    # in the same character

    # Test UTF-8
    decode_error_test(b'\xc0\x80', "add_one_codepoint",
                      b'\xc0\x80a', "UTF-8", True)

    # Test UTF-16LE
    decode_error_test(b'\xff\xfe', "add_utf16_bytes",
                      b'\xff\xfe\xff\xfea\x00', "UTF-16", True)

    # Test UTF-16BE
    decode_error_test(b'\xfe\xff', "add_utf16_bytes",
                      b'\xfe\xff\xfe\xffa\x00', "UTF-16", True)

    # Test UTF-32LE
    decode_error_test(b'\xff\xfe\x00\x00', "add_utf32_bytes",
                      b'\xff\xfe\x00\x00\xff\xfe\x00\x
