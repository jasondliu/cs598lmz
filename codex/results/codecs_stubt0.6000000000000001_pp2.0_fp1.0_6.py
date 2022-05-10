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
    # Test UnicodeDecodeError, UnicodeEncodeError and UnicodeTranslateError
    # behaviour with named attributes and the start attribute
    import _testcapi
    errors = ['strict', 'replace', 'ignore', 'backslashreplace', 'namereplace',
              'surrogateescape', 'surrogatepass',
              'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes']
    for error in errors:
        # test UnicodeDecodeError
        try:
            b'\xff'.decode('ascii', error)
        except UnicodeDecodeError as exc:
            assert exc.encoding == 'ascii'
            assert exc.object == b'\xff'
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == 'ordinal not in range(128)'
            assert exc.args == (
                b'\xff', 0, 1, 'ordinal not in range(128)')
        else:
            raise AssertionError('UnicodeDec
