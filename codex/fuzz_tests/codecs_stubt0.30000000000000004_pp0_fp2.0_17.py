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

def test_utf8_decode_error_handling():
    # Issue #8297: UTF-8 decoding errors should be handled properly
    # by the surrogatepass error handler.
    for i in range(0x80, 0x100):
        s = bytes([i])
        for j in range(1, 5):
            s += bytes([0x80 + (i & 0x3f)]) * j
        for j in range(1, 5):
            s += bytes([0x80 + (i & 0x3f)]) * j
            s += bytes([0xc0 + (i >> 6)])
            try:
                s.decode("utf-8", "surrogatepass")
            except UnicodeDecodeError as e:
                assert e.object is s
                assert e.end == len(s)
                assert e.start == len(s) - j - 1
                assert e.reason == "unexpected end of data"

def test_utf8_decode_error_handling_2():
    # Issue #8297: UTF-8 decoding
