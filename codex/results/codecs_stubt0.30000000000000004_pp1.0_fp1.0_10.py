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
    # test utf-8
    assert codecs.decode("\xc3\x28", "utf-8", "add_one_codepoint") == "a("
    assert codecs.decode("\xe2\x28\xa1", "utf-8", "add_one_codepoint") == "a(?"
    assert codecs.decode("\xe2\x82\x28", "utf-8", "add_one_codepoint") == "a("
    assert codecs.decode("\xf0\x90\x28\xbc", "utf-8", "add_one_codepoint") == "a(?"
    assert codecs.decode("\xf0\x28\x8c\xbc", "utf-8", "add_one_codepoint") == "a(?"
    assert codecs.decode("\xf0\x90\x90\x28", "utf-8", "add_one_codepoint") == "a("
    assert codecs.decode
