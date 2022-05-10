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

def test_unicode_error():
    ue = UnicodeError("a", b"xyz", 1, 2, "a")
    assert ue.start == 1
    assert ue.end == 2
    assert ue.reason == "a"

    e = ue.encode("ascii")
    assert type(e) is UnicodeEncodeError

    d = e.decode("ascii")
    assert type(d) is UnicodeDecodeError

    t = d.translate("ascii")
    assert type(t) is UnicodeTranslateError

    assert ue.__str__() == "'ascii' codec can't encode character 'x' in position 1: a"
    assert ue.__repr__() == "UnicodeError('a', 'xyz', 1, 2, 'a')"

    ue = UnicodeError("a", b"xyz", 1, 2, "a")
    assert ue.__str__() == "'a' codec can't decode byte 0x78 in position 1: a"
    assert ue.
