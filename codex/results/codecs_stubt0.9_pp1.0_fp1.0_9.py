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

def test_errorhandlers(src1, src2):
    for errorhandler_name in ("add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
        assert(unicode(src1, 'ascii', errorhandler_name) == u'abc')
        assert(unicode(src2, 'ascii', errorhandler_name) == u'abc\u1234')
    
def test_encode_errorhandler():
    cases = [
    # From test_unicode.py
        # surrogate pairs
        (u'\udc80\udc00', 'add_one_codepoint', '\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd'),
        # 3 byte UTF-8
        (u'\u0760', 'add_one_codepoint', '\u0760\ufffd'),
        (u'\u0760', 'add_utf16_bytes', '\u0760\ufffd'),
        (u'\u0760', '
