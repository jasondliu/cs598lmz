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

def test_error_handler_state():
    # see issue #14056
    state = {}
    def handler(exc):
        if not isinstance(exc, UnicodeEncodeError):
            raise TypeError("don't know how to handle %r" % exc)
        state['tried'] = True
        return (u'', exc.start + 1)
    codecs.register_error("test.error_handler_state", handler)
    u"\uffff\uffff".encode("ascii", "test.error_handler_state")
    assert state['tried']


def test_lone_surrogates():
    # see issue #14056
    for c in u'\ud800', u'\udfff':
        for errors in 'strict', 'replace', 'ignore':
            assert c.encode('utf-8', errors) == b''
            assert c.encode('utf-16', errors) == b'\xff\xfd'
            assert c.encode('utf-32', errors) == b'\x00\x
