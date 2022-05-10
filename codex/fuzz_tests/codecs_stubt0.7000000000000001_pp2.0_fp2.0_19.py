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
    if sys.platform != "win32":
        raise TestSkipped, "this test only runs on win32"

    import _codecs_cn
    s = "hello world"
    for encoding in "gbk", "gb2312", "gb18030", "hz":
        f = _codecs_cn.getcodec(encoding).streamreader
        r = f(io.BytesIO(s.encode(encoding)))
        assert r.read(1) == "h"
        assert r.read(1) == "e"
        assert r.read(1) == "l"
        assert r.read(1) == "l"
        assert r.read(1) == "o"
        assert r.read(1) == " "
        assert r.read(1) == "w"
        assert r.read(1) == "o"
        assert r.read(1) == "r"
        assert r.read(1) == "l"
        assert r.read(1) ==
