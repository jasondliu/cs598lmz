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
    # UnicodeEncodeError
    try:
        '\ud800'.encode('utf-8')
    except UnicodeEncodeError as exc:
        assert exc.object == '\ud800'
        assert exc.encoding == 'utf-8'
        assert exc.start == 0
        assert exc.end == 1
        assert exc.reason == 'surrogates not allowed'
        assert str(exc) == "'utf-8' codec can't encode character '\\ud800' in position 0: surrogates not allowed"
        assert exc.__reduce__() == (UnicodeEncodeError, ('\ud800', 'utf-8', 0, 1, 'surrogates not allowed'))
        assert exc.__reduce_ex__(1) == (UnicodeEncodeError, ('\ud800', 'utf-8', 0, 1, 'surrogates not allowed'))
        assert exc.__reduce_ex__(2) == (UnicodeEncodeError, ('\ud800', 'utf-8', 0, 1, 'surrog
