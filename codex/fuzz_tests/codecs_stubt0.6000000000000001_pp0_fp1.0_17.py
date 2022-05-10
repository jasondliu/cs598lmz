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

def check_error_handling(encoding, first, last):
    with codecs.open(TESTFN, "wb", encoding) as f:
        f.write("a")
    with codecs.open(TESTFN, "rb", encoding) as f:
        data = f.read()
    os.unlink(TESTFN)
    if data != b"a":
        raise AssertionError("codec %s returned unexpected bytes: %r" %
                             (encoding, data))
    try:
        data.decode(encoding)
    except UnicodeDecodeError as exc:
        if exc.start != 0 or exc.end != 1 or exc.reason != "add_one_codepoint":
            raise AssertionError("unexpected decode error: %r" % exc)
    else:
        raise AsserterError("decode error not raised")
    try:
        codecs.decode(data, encoding)
    except UnicodeDecodeError as exc:
        if exc.start != 0 or exc.end != 1 or exc.reason
