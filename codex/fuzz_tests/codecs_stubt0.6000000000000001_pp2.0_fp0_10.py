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

def test_errorhandler():
    assert u'\uffff'.encode('ascii', 'add_one_codepoint') == b'a\xff'
    assert u'\uffff'.encode('utf-16', 'add_one_codepoint') == b'\xff\xfea\x00'
    assert u'\uffff'.encode('utf-32', 'add_one_codepoint') == b'\xff\xfe\x00\x00a\x00\x00\x00'
    assert b'\x80'.decode('ascii', 'add_one_codepoint') == u'a'
    assert b'\xff\xfe'.decode('utf-16', 'add_one_codepoint') == u'a'
    assert b'\xff\xfe\x00\x00'.decode('utf-32', 'add_one_codepoint') == u'a'

    assert u'\uffff'.encode('utf-16', 'add_utf16_bytes') == b'
