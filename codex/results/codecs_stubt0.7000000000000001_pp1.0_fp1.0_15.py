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

def run_test_add_one_codepoint(encoding):
    f = codecs.getreader(encoding)
    r = f(io.BytesIO(b'\xff\xff'))
    s = r.read()
    assert s == 'a\uffff'
    assert len(s) == 2

def run_test_add_utf16_bytes(encoding):
    f = codecs.getreader(encoding)
    r = f(io.BytesIO(b'\xff\xff'))
    s = r.read()
    assert s == 'ab\uffff'
    assert len(s) == 3

def run_test_add_utf32_bytes(encoding):
    f = codecs.getreader(encoding)
    r = f(io.BytesIO(b'\xff\xff'))
    s = r.read()
    assert s == 'ab\uffff'
    assert len(s) == 3

def run_test_add_utf16_bytes_2(encoding):
    f =
