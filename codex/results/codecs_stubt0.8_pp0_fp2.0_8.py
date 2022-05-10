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
    if 1:
        print('BEGIN TEST')
        print('==========')
    else:
        print('SKIP')

    try:
        1.encode('undefined')
    except LookupError:
        pass
    else:
        print('test didn\'t raise the LookupError exception')

    assert '//IGNORE'.encode('string_escape') == '\\\n'

    assert ''.center(10, '+') == '++++++'
    assert 'x'.center(4,'+') == '+x+'

    assert '\u0141'.encode('0x_codec') == b'0x141'
    assert '\u0141'.encode('0x_codec') == b'0x141'
    assert '\u0141'.encode('0x_codec') == b'0x141'
    assert '\u0141'.encode('0x_codec') == b'0x141'
    assert '\u0141'.encode('0x_codec')
