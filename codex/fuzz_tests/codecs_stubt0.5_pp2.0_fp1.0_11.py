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

# test unicode escape decode
def test_unicode_escape_decode():
    assert '\x00'.decode('unicode-escape') == '\x00'
    assert 'a'.decode('unicode-escape') == 'a'
    assert '\\'.decode('unicode-escape') == '\\'
    assert '\\a'.decode('unicode-escape') == '\\a'
    assert '\\\n'.decode('unicode-escape') == '\\\n'
    assert '\\7'.decode('unicode-escape') == '\\7'
    assert '\\77'.decode('unicode-escape') == '\\77'
    assert '\\377'.decode('unicode-escape') == '\\377'
    assert '\\7777'.decode('unicode-escape') == '\\7777'
    assert '\\x00'.decode('unicode-escape') == '\x00'
    assert '\\x7f'.decode('unicode-escape') == '\x7f'
    assert '\\x7
