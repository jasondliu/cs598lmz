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

# Test the codecs module

# Test the UTF-8 codec

def test_utf8(encoding):
    assert codecs.lookup(encoding) is codecs.lookup('utf-8')
    assert codecs.lookup(encoding).name == 'utf-8'
    assert codecs.lookup(encoding).encode('\u20ac') == b'\xe2\x82\xac'
    assert codecs.lookup(encoding).decode(b'\xe2\x82\xac') == '\u20ac'
    assert codecs.lookup(encoding).decode(b'\xe2\x82\xac', 'strict') == '\u20ac'
    assert codecs.lookup(encoding).decode(b'\xe2\x82', 'strict') == '\ufffd\ufffd'
    assert codecs.lookup(encoding).decode(b'\xe2\x82', 'ignore') == ''
    assert codecs.lookup(encoding).decode
