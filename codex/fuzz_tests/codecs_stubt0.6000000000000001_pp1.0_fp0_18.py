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

# http://www.cl.cam.ac.uk/~mgk25/unicode.html#utf-8

utf8_boms = [
    # BOM, BOM+"a", BOM+"a"+BOM
    (b"\xef\xbb\xbf", b"\xef\xbb\xbf"+b"a", b"\xef\xbb\xbf"+b"a"+b"\xef\xbb\xbf"),
    (b"\xfe\xff", b"\xfe\xff"+b"a", b"\xfe\xff"+b"a"+b"\xfe\xff"),
    (b"\xff\xfe", b"\xff\xfe"+b"a", b"\xff\xfe"+b"a"+b"\xff\xfe"),
    (b"\x00\x00\xfe\xff", b"\x00\x00\xfe\xff"+b"a", b"\x00\x
