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

# Test the error handler
def test_error_handler():
    # Test the backslashreplace error handler
    assert b'abcd'.decode('ascii', 'backslashreplace') == r'abcd'
    assert b'ab\x80cd'.decode('ascii', 'backslashreplace') == r'ab\x80cd'
    assert b'ab\xc0cd'.decode('ascii', 'backslashreplace') == r'ab\x80cd'
    assert b'ab\xc0\x80cd'.decode('ascii', 'backslashreplace') == r'ab\x80\x80cd'
    assert b'ab\xc0\xc0cd'.decode('ascii', 'backslashreplace') == r'ab\x80\x80cd'

    # Test the xmlcharrefreplace error handler
    assert b'abcd'.decode('ascii', 'xmlcharrefreplace') == 'abcd'
    assert b'ab\x80cd'.decode('ascii', 'xmlchar
