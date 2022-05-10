import codecs
# Test codecs.register_error with test_pyio.
# Issue #17953: Verify that errors are reported only for code points above
# 0x10ffff.
for name in ('ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace', 'xmlcharrefreplace'):
    encoder = codecs.getincrementalencoder('utf-16le')(name)
    encoder.encode(u'\ue000')
    for char in range(0x110000):
        try:
            encoder.encode(unichr(char))
        except UnicodeEncodeError:
            pass


def test_read1():
    inp = io.BytesIO(b"abcde")
    f = io.TextIOWrapper(inp, "ascii")
    assert f.read(1) == 'a'
    assert f.read(2) == 'bc'
    assert f.read(3) == 'de'
    assert f.read(4) == ''


def test_read2():
    inp = io.BytesIO(b"abcde")
    f
