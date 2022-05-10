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

def test_utf7():
    # UTF-7
    assert bytes(b'a').decode('utf-7') == 'a'
    raises(UnicodeDecodeError, str, b'+', 'utf-7')
    raises(UnicodeDecodeError, str, b'+-', 'utf-7')
    raises(UnicodeDecodeError, str, b'+A', 'utf-7')
    raises(UnicodeDecodeError, str, b'+/', 'utf-7')
    raises(UnicodeDecodeError, str, b'+/a', 'utf-7')
    assert str(b'+MeQ-', 'utf-7') == '\u0644\u064A\u0647'
    assert str(b'+MgALMwAPE-', 'utf-7') == '\U00010348'
    assert str(b'+AOQ-', 'utf-7') == '\ufffe'
    assert str(b'+//8-', 'utf-7') == '\
