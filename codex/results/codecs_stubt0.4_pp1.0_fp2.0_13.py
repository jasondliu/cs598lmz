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

def test_unicode_error_init():
    # Test UnicodeError constructor
    exc = UnicodeError()
    assert exc.start == 0
    assert exc.end == 0
    assert exc.reason == None
    assert exc.object == None
    assert exc.encoding == None
    assert exc.args == (None, None, 0, 0, None)

    exc = UnicodeError('reason')
    assert exc.start == 0
    assert exc.end == 0
    assert exc.reason == 'reason'
    assert exc.object == None
    assert exc.encoding == None
    assert exc.args == ('reason', None, 0, 0, None)

    exc = UnicodeError('reason', 'object')
    assert exc.start == 0
    assert exc.end == 0
    assert exc.reason == 'reason'
    assert exc.object == 'object'
    assert exc.encoding == None
    assert exc.args == ('reason', 'object', 0, 0, None)

    exc = UnicodeError('reason', 'object', 1)
    assert exc.start == 1
   
