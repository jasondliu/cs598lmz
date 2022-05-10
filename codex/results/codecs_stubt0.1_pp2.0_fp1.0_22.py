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
    # Test UTF-8
    for encoding in ("utf-8", "utf_8"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint"):
            for input, expected in (
                (b'\xc3\x28', u'\ufffd('),
                (b'\xa0\xa1', u'\ufffd\ufffd'),
                (b'\xe2\x28\xa1', u'\ufffd(\ufffd'),
                (b'\xe2\x82\x28', u'\ufffd\u07c0('),
                (b'\xf0\x90\x28\xbc', u'\U0001d11e\ufffd'),
                (b'\xf0\x28\x8c\xbc', u'\ufffd\ufffd\ufffd'),
                (b'\xf0\x90\x28\x28', u'\U0001d11e\ufffd('),
                (b'\xf8\
