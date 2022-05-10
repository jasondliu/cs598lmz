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

def test_utf8_decode_errors():
    # utf-8 codec
    u = '\u3042'
    for i in range(len(u.encode('utf-8'))):
        for j in range(i, len(u.encode('utf-8'))):
            s = u.encode('utf-8')[:i] + b'\xff' + u.encode('utf-8')[j+1:]
            try:
                s.decode('utf-8')
            except UnicodeDecodeError as exc:
                assert exc.object is s
                assert exc.start == i
                assert exc.end == j+1
                assert exc.reason == 'invalid start byte'
                assert exc.encoding == 'utf-8'
                assert str(exc) == "('utf-8', %r, %d, %d, 'invalid start byte')" % (s, i, j+1)
                assert exc.startswith(s.decode('utf-8', 'ignore'))
                assert exc.
