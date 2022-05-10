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

# Note that the errors are tested in the same order as for the
# standard error handlers.

# UnicodeDecodeError

def test_unicode_decode_error():
    # test UnicodeDecodeError

    # test the standard handler
    s = b'f\xed\xf9\xec'
    for handler in (None, 'strict', 'replace', 'ignore', 'surrogateescape',
                    'backslashreplace', 'xmlcharrefreplace'):
        if handler is None:
            u = s.decode('ascii')
        else:
            u = s.decode('ascii', handler)
        assert isinstance(u, unicode)

    # test the 'add_one_codepoint' handler
    u = s.decode('ascii', 'add_one_codepoint')
    assert isinstance(u, unicode)
    assert u == 'fa\udcf1'

    # test the 'add_utf16_bytes' handler
    u = s.decode('ascii', 'add_utf16
