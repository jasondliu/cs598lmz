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
    with support.check_warnings(('', UnicodeWarning)):
        for encoding in ('utf-8', 'utf-16', 'utf-32'):
            for input, expected in [
                    ('\x80', '\ufffd'),
                    ('\x80\x80', '\ufffd\ufffd'),
                    ('\x80\x80\x80', '\ufffd\ufffd\ufffd'),
                    ('\x80\x80\x80\x80', '\ufffd\ufffd\ufffd\ufffd'),
                    ]:
                u = input.decode(encoding, 'replace')
                support.verbose('%s -> %s', repr(input), repr(u))
                if u != expected:
                    raise support.TestFailed("%s.decode('%s', 'replace') -> %s != %s" %
                                             (repr(input), encoding, repr(u), repr(expected)))

            for input, expected in [
                    ('\x80', 'a\ufffd'),
                   
