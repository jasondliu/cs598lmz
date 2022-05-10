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

try:
    u"abc\ud800".encode("utf-8", "add_one_codepoint")
except UnicodeEncodeError as e:
    assert e.object == u"abc\ud800"
    assert e.start == 3
    assert e.end == None
    assert e.reason == "add_one_codepoint"
    assert str(e) == "codec.add_one_codepoint: 'utf-8' codec can't encode character '\\ud800' in position 3: ordinal not in range(128)"
else:
    raise AssertionError()

try:
    u"abc\ud800".encode("utf-16", "add_one_codepoint")
except UnicodeEncodeError as e:
    assert e.object == u"abc\ud800"
    assert e.start == 3
    assert e.end == None
    assert e.reason == "add_one_codepoint"
    assert str(e) == "codec.add_one_codepoint: 'utf-16' codec can't encode
