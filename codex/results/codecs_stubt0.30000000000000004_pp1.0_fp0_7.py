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
    # Test utf-16
    for (encoding, errors) in [("utf-16", "strict"),
                               ("utf-16", "ignore"),
                               ("utf-16", "replace"),
                               ("utf-16", "add_one_codepoint"),
                               ("utf-16", "add_utf16_bytes")]:
        # Test decoding
        for (input, output) in [
            (b'\xff\xfe\x00\x61\x00\x62\x00\x63',
             'abc'),
            (b'\xff\xfe\x00\x61\x00\x62\x00\x63\x00\x64',
             'abcd'),
            (b'\xff\xfe\x00\x61\x00\x62\x00\x63\x00\x64\x00\x65',
             'abcde'),
            (b'\xff\xfe\x00\x61\x00\x62\x00\x
