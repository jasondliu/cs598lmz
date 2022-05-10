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

def test_utf8():
    # UTF-8
    #
    #    U+000000 - U+00007F: 0xxxxxxx
    #    U+000080 - U+0007FF: 110xxxxx 10xxxxxx
    #    U+000800 - U+00FFFF: 1110xxxx 10xxxxxx 10xxxxxx
    #    U+010000 - U+10FFFF: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
    #
    # Invalid sequences:
    #
    #    [80-BF] after [C0-C1]
    #    [80-BF] after [E0] and not in [A0-BF]
    #    [80-BF] after [F0] and not in [90-BF]
    #    [80-8F] after [F1-F3]
    #    [80-BF] after [F4] and not in [80-8F]
    #    [A0-BF] after [E0]
    #    [90-BF] after [F0]
    #    [80-8
