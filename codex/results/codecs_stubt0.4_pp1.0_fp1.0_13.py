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
    def test_decode(encoding, input, errors, expected):
        assert codecs.decode(input, encoding, errors) == expected

    # Test that the "add_one_codepoint" error handler works.
    test_decode('ascii', b'\xff', 'add_one_codepoint', 'a\ufffd')
    test_decode('ascii', b'\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd')
    test_decode('ascii', b'\xff\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd\ufffd')
    test_decode('utf-8', b'\xff', 'add_one_codepoint', 'a\ufffd')
    test_decode('utf-8', b'\xff\xff', 'add_one_codepoint', 'a\ufffd\ufffd')
    test_decode('utf-8', b'\xff\xff\xff',
