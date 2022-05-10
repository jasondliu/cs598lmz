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

def check(decoder, encoder, input, errors, expected):
    input = input.encode(encoder, errors)
    actual = input.decode(decoder, errors)
    if actual != expected:
        raise AssertionError('%r.decode(%r, %r) == %r != %r' %
                             (input, decoder, errors, actual, expected))

def check_code_units(decoder, encoder, input, errors, expected):
    input = input.encode(encoder, errors)
    actual = list(codecs.iterdecode(iter([input]), decoder, errors))
    if actual != [expected]:
        raise AssertionError('%r.decode(%r, %r) == %r != %r' %
                             (input, decoder, errors, actual, [expected]))

def test_surrogate_handling():
    # On Windows, surrogate pairs are not allowed in filenames (Latin-1
    # surrogate pairs are).
    if sys.platform == 'win32':
