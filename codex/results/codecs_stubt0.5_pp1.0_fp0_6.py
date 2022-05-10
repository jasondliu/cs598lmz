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
    try:
        u'\udc80'.encode('utf-7')
    except UnicodeEncodeError as e:
        assert e.object == u'\udc80'
        assert e.encoding == 'utf-7'
        assert e.reason == 'surrogates not allowed'
        assert e.start == 0
        assert e.end == 1
        assert e.args[0] == 'surrogates not allowed'
    else:
        assert False, "UnicodeEncodeError not raised"

    try:
        b'\x80'.decode('utf-8')
    except UnicodeDecodeError as e:
        assert e.object == b'\x80'
        assert e.encoding == 'utf-8'
        assert e.reason == 'invalid start byte'
        assert e.start == 0
        assert e.end == 1
        assert e.args[0] == 'invalid start byte'
    else:
        assert False, "UnicodeDecodeError not raised"

    try:
       
