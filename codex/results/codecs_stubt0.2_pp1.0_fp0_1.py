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
    for encoding in ("utf-8", "utf_8"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for input, expected in [
                (b'\x80', u'\ufffd'),
                (b'\xc0', u'\ufffd'),
                (b'\xc0\x80', u'\ufffd\ufffd'),
                (b'\xc0\x80\xc0\x80', u'\ufffd\ufffd\ufffd\ufffd'),
                (b'\xc0\x80\xc0\x80\xc0\x80', u'\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'),
                (b'\xc0\x80\xc0\x80\xc0\x80\xc0\x80', u'\ufffd\ufffd\ufffd\ufffd\
