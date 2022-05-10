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
    import sys
    if sys.maxunicode == 0xffff:
        # UCS2 build
        tests = [
            # UCS2 build: errorhandler must return a unicode object
            (b'a\xff', 'ascii', None, None, 0, 1, 'add_one_codepoint',
             "\uFFFD", '\uFFFD'),
            (b'a\xff', 'utf-16', None, None, 0, 2, 'add_utf16_bytes',
             "\uFFFD", '\uFFFD'),
            (b'a\xff', 'utf-32', None, None, 0, 4, 'add_utf32_bytes',
             "\uFFFD", '\uFFFD'),
            (b'\xff', 'iso8859-1', None, None, 0, 1, 'add_one_codepoint',
             "\uFFFD", '\uFFFD'),
            (b'\xff', 'iso8859-15', None, None, 0, 1, 'add_one_codep
