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
    assert codecs.decode(b'\x80', 'utf-8', 'replace') == '\ufffd'
    assert codecs.decode(b'\x80', 'utf-8', 'ignore') == ''
    assert codecs.decode(b'\x80', 'utf-8', 'backslashreplace') == r'\x80'
    try:
        codecs.decode(b'\x80', 'utf-8', 'add_one_codepoint')
    except UnicodeDecodeError as e:
        assert e.object == b'\x80'
        assert e.start == 0
        assert e.end == 1
        assert e.reason == 'illegal code point'
    else:
        raise AssertionError('Did not raise UnicodeDecodeError')

    assert codecs.decode(b'\x80', 'utf-16', 'ignore') == ''
    try:
        codecs.decode(b'\x80', 'utf-16', 'add_utf16_bytes')
   
