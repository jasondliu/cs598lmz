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

#
# Test UTF-7
#

def test_utf7_encode():
    assert utf_7.encode('a') == b'a'
    assert utf_7.encode('\u203E') == b'~'
    assert utf_7.encode('\u203E', 'replace') == b'?'
    assert utf_7.encode('\u203E', 'xmlcharrefreplace') == b'&#8254;'
    assert utf_7.encode('a\u203E', 'strict') == b'a+APw-'
    assert utf_7.encode('a\u203E', 'strict', 'replace') == b'a+APw-?'
    assert utf_7.encode('a\u203E', 'strict', 'xmlcharrefreplace') == b'a+APw-&#8254;'
    assert utf_7.encode('a\u203E', 'strict', add_one_codepoint) == b'a+APw-
