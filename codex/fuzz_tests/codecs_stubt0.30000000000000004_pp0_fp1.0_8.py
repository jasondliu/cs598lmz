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
    # test UnicodeEncodeError
    for encoding in ('ascii', 'latin-1', 'utf-16', 'utf-32'):
        try:
            u'\U0010ffff'.encode(encoding)
        except UnicodeEncodeError as exc:
            if encoding == 'ascii':
                assert exc.object == u'\U0010ffff'
                assert exc.encoding == 'ascii'
                assert exc.start == 0
                assert exc.end == 1
                assert exc.reason == 'illegal Unicode character'
                assert exc.object[exc.start:exc.end] == u'\U0010ffff'
                assert str(exc) == "'ascii' codec can't encode character '\\U0010ffff' in position 0: illegal Unicode character"
            elif encoding == 'latin-1':
                assert exc.object == u'\U0010ffff'
                assert exc.encoding == 'latin-1'
                assert exc.start == 0
                assert exc.end == 1
                assert exc.reason == '
