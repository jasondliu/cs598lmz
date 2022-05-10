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

#
#    Test UnicodeEncodeError
#

a = '\u1234'

def test_strict(encoding):
    try:
        a.encode(encoding, 'strict')
    except UnicodeEncodeError as exc:
        assert exc.encoding == encoding
        assert exc.object == a
        assert exc.start == 0
        assert exc.end == 1
    else:
        raise Exception("strict encoding failed to raise UnicodeEncodeError")

def test_ignore(encoding):
    assert a.encode(encoding, 'ignore') == b''

def test_replace(encoding):
    assert a.encode(encoding, 'replace') == b'?'

def test_xmlcharrefreplace(encoding):
    assert a.encode(encoding, 'xmlcharrefreplace') == b'&#4660;'

def test_backslashreplace(encoding):
    assert a.encode(encoding, 'backslashreplace') == b'\\u1234'

def test_namereplace(
