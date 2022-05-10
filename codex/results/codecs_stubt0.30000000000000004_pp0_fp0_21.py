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
    # test UTF-8
    for i in range(0xD800, 0xE000):
        if i != 0xDFFF:
            # surrogates are not allowed in UTF-8
            assert codecs.utf_8_decode(chr(i).encode("utf-8"))[0] == "\ufffd"
            assert codecs.utf_8_decode(chr(i).encode("utf-8"), "replace")[0] == "\ufffd"
            assert codecs.utf_8_decode(chr(i).encode("utf-8"), "ignore")[0] == ""
            assert codecs.utf_8_decode(chr(i).encode("utf-8"), "add_one_codepoint")[0] == "a"
            assert codecs.utf_8_decode(chr(i).encode("utf-8"), "add_utf16_bytes")[0] == "\ufffd"
            assert codecs.utf_8_decode(chr(i
