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
    # Test codecs.decode()
    assert codecs.decode('abc', 'ascii') == b'abc'
    assert codecs.decode('abc', 'ascii', 'replace') == b'abc'
    assert codecs.decode('abc\xff', 'ascii', 'replace') == b'abc?'
    assert codecs.decode('abc\xff', 'ascii', 'ignore') == b'abc'
    assert codecs.decode('abc\xff', 'ascii', 'backslashreplace') == b'abc\\xff'
    assert codecs.decode('abc\xff', 'ascii', 'xmlcharrefreplace') == b'abc&#255;'
    assert codecs.decode('abc\xff', 'ascii', 'add_one_codepoint') == b'abca'
    assert codecs.decode('abc\xff', 'ascii', 'add_utf16_bytes') == b'abca\xff'
    assert codecs.decode('abc
