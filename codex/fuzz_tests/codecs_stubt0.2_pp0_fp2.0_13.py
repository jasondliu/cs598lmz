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
    # Test UnicodeEncodeError
    for encoding in ('ascii', 'latin-1', 'utf-8', 'utf-16', 'utf-32'):
        try:
            u'\ud800'.encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.object == u'\ud800'
            assert exc.encoding == encoding
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == 'surrogates not allowed'
            assert str(exc) == '\'utf-8\' codec can\'t encode character ' \
                               '\\ud800 in position 0: surrogates not allowed'
            assert repr(exc) == "UnicodeEncodeError('%s', u'\\ud800', 0, 1, 'surrogates not allowed')" % encoding
            assert exc.__reduce__() == (UnicodeEncodeError, (encoding, u'\ud800', 0, 1, 'surrogates not allowed'))
            assert exc.__reduce_ex
