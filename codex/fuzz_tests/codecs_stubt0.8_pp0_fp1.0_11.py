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

test_data = [
    [b'aaa\xff', 0, u'aaa\ufffd', 0],
    [b'aaa\xff', 1, u'a\ufffdaa', 2],
    [b'aaa\xff', 2, u'aa\ufffd', 2],
    [b'aaa\xff', 2, u'aa\ua000', 2, "add_one_codepoint"],
    [b'aaa\xff', 2, u'aa\uabcd', 2, "add_one_codepoint"],

    [b'aaa\xff', 1, u'a\ufffdaa', 2, "add_utf16_bytes"],
    [b'\xffaaa', 1, u'\ufffd\ufffdaa', 2, "add_utf16_bytes"],
    [b'aaa\xff', 2, u'aa\ufffd', 2, "add_utf16_bytes"],
    [b'\xffaaa', 2, u'\ufffd\ufffdaa', 3, "add_utf16_bytes"],
    [b'
