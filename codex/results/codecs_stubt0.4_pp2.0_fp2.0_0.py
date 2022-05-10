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
    # Test UTF-8 surrogates
    for x in [0xD800, 0xDFFF]:
        try:
            ''.encode('utf-8', 'surrogatepass')
        except UnicodeEncodeError as e:
            assert e.object == chr(x), "expected %r, got %r" % (chr(x), e.object)
            assert e.start == 0, "expected 0, got %d" % e.start
            assert e.end == 1, "expected 1, got %d" % e.end

    # Test UTF-8 surrogates
    for x in [0xD800, 0xDFFF]:
        try:
            ''.encode('utf-8', 'surrogateescape')
        except UnicodeEncodeError as e:
            assert e.object == chr(x), "expected %r, got %r" % (chr(x), e.object)
            assert e.start == 0, "expected 0, got %d" % e.start
            assert e.end ==
