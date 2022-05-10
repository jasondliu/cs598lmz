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
        for errors in ("strict", "replace", "ignore", "add_one_codepoint"):
            for input, output in (
                (b"\xc3\x28", ""),
                (b"\xa0\xa1", "\ufffd\ufffd"),
                (b"\xe2\x28\xa1", "\ufffd"),
                (b"\xe2\x82\x28", "\ufffd"),
                (b"\xf0\x90\x28\xbc", "\U00010348"),
                (b"\xf0\x28\x8c\xbc", "\ufffd"),
                (b"\xf0\x90\x90\x28", "\U00010348"),
                (b"\xf8\xa1\xa1\xa1\xa1", "\ufffd"),
                (b"\xfc\xa1\xa1\xa1\xa1\xa1", "\
