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

def show_codepoints(s):
    for c in s:
        print(hex(ord(c)), end=' ')
    print()

def show_bytes(s):
    for b in s:
        print(hex(b), end=' ')
    print()

def test_encode():
    assert b'ab' == '\xFF'.encode('ascii', 'add_one_codepoint')
    assert b'abcd' == '\xFF'.encode('utf-16', 'add_one_codepoint')
    assert b'abcd' == '\xFF'.encode('utf-32', 'add_one_codepoint')
    assert b'ab' == '\xFF'.encode('utf-16', 'add_utf16_bytes')
    assert b'abcd' == '\xFF'.encode('utf-32', 'add_utf32_bytes')

def test_decode():
    assert 'ab' == b'\xFF'.decode('ascii', 'add_one
