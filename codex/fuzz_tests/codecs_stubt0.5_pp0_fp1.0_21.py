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
    # utf-8 with surrogateescape error handler
    test_unicode('utf-8', '\ud800', '\xff', '\ud800\xff')
    test_unicode('utf-8', '\udc00', '\xff', '\udc00\xff')
    test_unicode('utf-8', '\ud800\udc00', '\xff', '\ud800\udc00\xff')
    test_unicode('utf-8', '\udbff\udfff', '\xff', '\udbff\udfff\xff')

    # utf-16 with surrogateescape error handler
    test_unicode('utf-16', '\ud800', '\xff', '\ud800\xff')
    test_unicode('utf-16', '\udc00', '\xff', '\udc00\xff')
    test_unicode('utf-16', '\ud800\udc00', '\xff', '\ud800\udc00\xff')
    test_unicode('
