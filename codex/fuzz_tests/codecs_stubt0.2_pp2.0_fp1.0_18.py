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

# test utf-8
for enc in ["utf-8", "utf_8"]:
    print("testing", enc)
    # test decoding
    for i in range(0x80, 0x100):
        s = bytes([i])
        try:
            s.decode(enc)
        except UnicodeDecodeError as exc:
            assert exc.object == s
            assert exc.encoding == enc
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "invalid start byte"
            assert exc.object[exc.start:exc.end] == bytes([i])
            assert exc.args == (s, 0, 1, "invalid start byte")
        else:
            assert False, "UnicodeDecodeError not raised"

    # test encoding
    for i in range(0xD800, 0xE000):
        s = chr(i)
        try:
            s.encode(enc)
        except UnicodeEncodeError as exc:
            assert exc.object == s
            assert exc.enc
