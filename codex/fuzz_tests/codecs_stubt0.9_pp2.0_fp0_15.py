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

invalid_utf8 = [b"\xc2\x80x", b"\xe0\x80x"]

def get_test_data(encoding, errors):
    return [(encoding, b'x', errors, "end {} with 'x'".format(encoding)),
            (encoding, b'x\xc2x', "ignore", "ignore 'x\\xc2' at the end of {}".format(encoding)),
            (encoding, b'x\xc2\x80x', "ignore", "ignore 'x\\xc2\\x80' at the end of {}".format(encoding)),
            (encoding, b'x\xe0\x80x', "ignore", "ignore 'x\\xe0\\x80' at the end of {}".format(encoding)),
            (encoding, b'x\xe0\x80\x80x', "replace", "replace 'x\\xe0\\x80\\x80' at the end of {}".format(encoding)),
            (encoding, b'x\xf0\x80x', "
