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

def test_reader():
    reader = codecs.getreader("utf-8")

    assert (reader(io.BytesIO(b"abc"))).read() == "abc"
    assert (reader(io.BytesIO(b"x\xF1"))).read() == "x\u00F1"
    assert (reader(io.BytesIO(b"x\xF1"), errors="strict")).read() == "x\u00F1"
    assert (reader(io.BytesIO(b"x\xF1"), errors="replace")).read() == "x?"
    assert (reader(io.BytesIO(b"x\xF1"), errors="add_one_codepoint")).read() == "x\u00F1a"
    assert (reader(io.BytesIO(b"\xF1"))).read() == "\u00F1"
    assert (reader(io.BytesIO(b"\xF1"), errors="strict", byteorder="<")).read() == "\u00F1"
    assert (reader(io
