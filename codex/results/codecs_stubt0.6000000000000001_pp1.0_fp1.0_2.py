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

buffer_encoding_errors = ['strict', 'ignore', 'replace', 'xmlcharrefreplace',
                          'backslashreplace', 'namereplace', 'add_one_codepoint',
                          'add_utf16_bytes', 'add_utf32_bytes']

def test_buffer_encoding_errors():
    """
    Test various error handling schemes in codecs
    """
    for error in buffer_encoding_errors:
        # Test unicode -> bytes
        b = u"\u1234".encode("ascii", error)
        if error in ('strict', 'ignore', 'replace'):
            assert b == (b'?' if error == 'replace' else b'')
        elif error == 'xmlcharrefreplace':
            assert b == b'&#4660;'
        elif error == 'backslashreplace':
            assert b == b'\\u1234'
        elif error == 'namereplace':
            assert b == b'\\N{ETHIOPIC SYLLABLE SEE}'
        elif error == '
