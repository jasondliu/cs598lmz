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

def getbytes(c):
    return c.encode('utf-8')

def test_unicodeescape_decode_add_one_codepoint():
    class State:
        def decode(self, input, errors):
            return self, input + '\u1234'
    state = State()
    to_decode = "a\\\n\r"
    decoded, length, state = codecs.unicode_escape_decode(to_decode, "add_one_codepoint", state)
    assert decoded == "a\u1234"
    assert length == len(to_decode) - 2
    assert state is None

def test_unicodeescape_decode_add_one_codepoint_with_error():
    class State:
        def decode(self, input, errors):
            return self, input + '\u1234'
    state = State()
    to_decode = "\\\n\r"
    decoded, length, state = codecs.unicode_escape_decode(to_dec
