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

def test_utf_16_be_errorhandler(tests):
    # test UTF-16-BE
    for (input, output) in tests:
        assert codecs.utf_16_be_decode(input, 'add_one_codepoint') == output
        assert codecs.utf_16_be_decode(input, 'add_utf16_bytes') == output
        assert codecs.utf_16_be_decode(input, 'add_utf32_bytes') == output

def test_utf_16_le_errorhandler(tests):
    # test UTF-16-LE
    for (input, output) in tests:
        assert codecs.utf_16_le_decode(input, 'add_one_codepoint') == output
        assert codecs.utf_16_le_decode(input, 'add_utf16_bytes') == output
        assert codecs.utf_16_le_decode(input, 'add_utf32_bytes') == output

def test_utf_16_ex_errorhandler(tests):
    #
