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
    # test the surrogatepass error handler
    for encoding in ('utf-16', 'utf-32'):
        for errors in ('surrogatepass', 'replace', 'ignore', 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
            for input in ('\ud800', '\udc00', '\ud800\udc00', '\ud800\udc00\ud800', '\ud800\udc00\ud800\udc00'):
                try:
                    input.encode(encoding, errors)
                except UnicodeEncodeError:
                    pass
                else:
                    raise AssertionError("%s.encode('%s', '%s') should have raised UnicodeEncodeError" % (repr(input), encoding, errors))

    # test the surrogateescape error handler
    for encoding in ('utf-16', 'utf-32'):
        for errors in ('surrogateescape', 'replace', 'ignore', 'add_one_codepoint', 'add_utf
