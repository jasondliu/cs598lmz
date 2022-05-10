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
    # UTF-8
    for errors in ["strict", "ignore", "replace", "add_one_codepoint"]:
        for i in range(0, 256):
            if i < 0x80:
                s = bytes([i])
            elif i < 0xc0:
                s = bytes([0xc0, i])
            elif i < 0xe0:
                s = bytes([0xe0, i, 0])
            elif i < 0xf0:
                s = bytes([0xf0, i, 0, 0])
            elif i < 0xf8:
                s = bytes([0xf8, i, 0, 0, 0])
            elif i < 0xfc:
                s = bytes([0xfc, i, 0, 0, 0, 0])
            elif i < 0xfe:
                s = bytes([0xfe, i, 0, 0, 0, 0, 0])
            else:
                s = bytes([0xff, i, 0, 0, 0, 0, 0, 0])
