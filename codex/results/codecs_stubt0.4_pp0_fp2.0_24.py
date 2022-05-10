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

def check_error_handling(encoding, input, expected):
    try:
        input.decode(encoding)
    except UnicodeDecodeError as exc:
        assert exc.object == input
        assert exc.start == 0
        assert exc.end == len(input)
        assert exc.reason == "unknown"
        assert exc.encoding == encoding
        assert exc.args[0] == "unknown codec can't decode byte 0x80 in position 0: %s" % repr(input)
        assert exc.args[1] == 0
        assert exc.args[2] == len(input)
        assert exc.args[3] == encoding
        assert exc.args[4] == "unknown"
        assert exc.args[5] == input
        assert exc.args[6] == (0, len(input))
        assert exc.args[7] == None

        try:
            input.decode(encoding, "strict")
        except UnicodeDecodeError as exc:
            assert exc.object == input
            assert exc.start == 0
            assert exc
