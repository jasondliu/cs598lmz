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

def test_codec_name_normalization():
    assert codecs.lookup('utf-8') is codecs.lookup('utf_8')
    assert codecs.lookup('utf-8') is codecs.lookup('UTF-8')
    assert codecs.lookup('utf-8') is codecs.lookup('Utf_8')
    assert codecs.lookup('utf-8') is codecs.lookup('uTf-8')

def test_search_function():
    import encodings.unicode_escape
    assert codecs.lookup(encodings.unicode_escape.__name__) is encodings.unicode_escape

def test_search_function_normalization():
    import encodings.unicode_escape
    assert codecs.lookup(encodings.unicode_escape.__name__.replace('_', '-')) is encodings.unicode_escape

def test_search_function_aliasing():
    import encodings.utf_8
    assert codecs.lookup('
