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

def test_decode_error():
    # Test UnicodeDecodeError
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        try:
            u'\uffff'.encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.object == u'\uffff'
            assert exc.encoding == encoding
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == 'surrogates not allowed'
            assert str(exc) == ("'%s' codec can't encode character '\\uffff' in position 0: "
                "surrogates not allowed" % encoding)
            assert repr(exc) == ("UnicodeEncodeError('%s', u'\\uffff', 0, 1, 'surrogates not allowed')" % encoding)
        else:
            assert False, "should have raised UnicodeEncodeError"

        try:
            u'\uffff'.encode(encoding, 'add_one_codepoint')
        except UnicodeEncodeError as exc:

