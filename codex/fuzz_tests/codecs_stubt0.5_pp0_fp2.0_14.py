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

def test_utf8(errorhandler):
    assert b'\xe9'.decode('utf-8', errorhandler) == 'é'
    assert b'\xe9\x80'.decode('utf-8', errorhandler) == 'é\x80'
    assert b'\xe9\x80\x80'.decode('utf-8', errorhandler) == 'é\x80\x80'

def test_utf16(errorhandler):
    assert b'\x00\xe9'.decode('utf-16', errorhandler) == 'é'
    assert b'\x00\xe9\x00\x80'.decode('utf-16', errorhandler) == 'é\x00\x80'
    assert b'\x00\xe9\x00\x80\x00\x80'.decode('utf-16', errorhandler) == 'é\x00\x80\x00\x80'

def test_utf32(errorhandler):
    assert b'\x00\x00\x00\xe9'.decode('
