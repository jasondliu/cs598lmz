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

def test_codecs_utf8_decode_error(space):
    w_exc = space.appexec([], """():
        try:
            "abc\xff".decode("utf-8")
        except UnicodeDecodeError as e:
            return e
        else:
            assert False
    """)
    assert space.eq_w(space.getattr(w_exc, space.wrap("start")),
                      space.wrap(3))
    assert space.eq_w(space.getattr(w_exc, space.wrap("end")),
                      space.wrap(4))
    assert space.eq_w(space.getattr(w_exc, space.wrap("object")),
                      space.wrap("abc\xff"))
    assert space.eq_w(space.getattr(w_exc, space.wrap("reason")),
                      space.wrap("invalid start byte"))

    w_exc = space.appexec([], """():
        try:
            "abc\xff".decode("utf-8", "replace")
        except Unicode
