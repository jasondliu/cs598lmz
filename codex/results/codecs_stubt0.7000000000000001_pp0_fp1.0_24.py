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
    # Test \U escape handler
    assert 'abcd' == 'a\\U0010ffffbcd'.encode('unicode_escape')
    assert 'a\U0010ffffbcd' == 'a\\\\U0010ffffbcd'.encode('unicode_escape')

    # Test hex codecs
    assert codecs.getdecoder('hex')('ff', 'strict') == (b'\xff', 2)
    assert codecs.getdecoder('hex')('f', 'strict') == (b'\x0f', 1)
    assert codecs.getdecoder('hex')('f', 'replace') == (b'?', 1)
    assert codecs.getdecoder('hex')('f', 'ignore') == (b'', 1)
    assert codecs.getdecoder('hex')('fA', 'replace') == (b'?', 1)
    assert codecs.getdecoder('hex')('fA', 'ignore') == (b'', 1)
    assert codecs.getencoder('hex'
