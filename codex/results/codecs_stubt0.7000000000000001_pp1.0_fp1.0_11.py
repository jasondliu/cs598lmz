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

with BytesIO() as f:
    f.write(b'\x00\xf0')
    f.seek(0)

    # UTF-16-BE
    r = codecs.getreader("utf-16-be")(f)
    assert r.read(1) == '\U0010FFFF'
    with raises(UnicodeDecodeError):
        r.read(1)

    f.seek(0)
    r = codecs.getreader("utf-16-be")(f, errors="ignore")
    assert r.read(2) == '\U0010FFFF'
    assert r.read(1) == ''

    f.seek(0)
    r = codecs.getreader("utf-16-be")(f, errors="replace")
    assert r.read(2) == '\U0010FFFF\ufffd'
    assert r.read(1) == '\ufffd'

    f.seek(0)
    r = codecs.getreader("utf-16-be")(f, errors="surrogateescape")
   
