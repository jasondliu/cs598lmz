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


def test_idna():
    # make sure that idna crashes don't leave the process with a broken
    # default encoding
    import _codecs
    orig_idna = _codecs.lookup('idna')

    def bad_idna(input, errors='strict'):
        raise ValueError('bad idna')

    _codecs.register('idna', bad_idna)

    try:
        s = '\u00f1'
        s.encode('idna')
    except ValueError:
        pass
    else:
        assert False

    # Make sure the default encoding is still 'ascii'
    assert 'ascii' == sys.getdefaultencoding()

    _codecs.register('idna', orig_idna)


def test_UTF16():
    # UTF-16 encoding tests

    input = "foo\u1234\u5678bar"
    expect_le = b"foo\x34\x12\x78\x56bar"
    expect_be = b"foo\x12
