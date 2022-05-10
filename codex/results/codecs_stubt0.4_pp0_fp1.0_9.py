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

def test_utf8_decode_errors():
    # Test UTF-8 decoding errors
    def check_decode(input, errorhandler, expected):
        decoded, consumed = codecs.utf_8_decode(input, errors=errorhandler)
        assert decoded == expected
        assert consumed == len(input)

    check_decode(b'\xff', 'strict', None)
    check_decode(b'\xff', 'ignore', '')
    check_decode(b'\xff', 'replace', '\ufffd')
    check_decode(b'\xff', 'add_one_codepoint', 'a')
    check_decode(b'\xff', 'add_utf16_bytes', '\ufffd')
    check_decode(b'\xff', 'add_utf32_bytes', '\ufffd')

    check_decode(b'\xff\xff', 'strict', None)
    check_decode(b'\xff\xff', 'ignore', '')
    check_decode(b'\
