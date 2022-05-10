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
    # Test the UTF-8 codec
    assert codecs.utf_8_decode(b'abc') == ('abc', 3)
    assert codecs.utf_8_decode(b'abc\xff') == ('abc\ufffd', 4)
    assert codecs.utf_8_decode(b'abc\xff', errors='ignore') == ('abc', 4)
    assert codecs.utf_8_decode(b'abc\xff', errors='replace') == ('abc\ufffd', 4)
    assert codecs.utf_8_decode(b'abc\xff', errors='surrogateescape') == ('abc\udcff', 4)
    assert codecs.utf_8_decode(b'abc\xff', errors='surrogatepass') == ('abc\udcff', 4)
    assert codecs.utf_8_decode(b'abc\xff', errors='xmlcharrefreplace') == ('abc&#255;', 4)
    assert codecs.utf_8_decode(b'abc\xff',
