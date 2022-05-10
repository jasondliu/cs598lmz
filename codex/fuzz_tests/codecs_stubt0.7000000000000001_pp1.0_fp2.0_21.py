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

# UnicodeEncodeError

e = UnicodeEncodeError("ascii", "\xff", 0, 1,
                       "ordinal not in range(128)")
try:
    raise e
except UnicodeEncodeError as e:
    assert e.encoding == "ascii"
    assert e.object == "\xff"
    assert e.start == 0
    assert e.end == 1
    assert e.reason == "ordinal not in range(128)"
    assert e.args == ("ascii", "\xff", 0, 1,
                      "ordinal not in range(128)")

assert e.encode("ascii", "add_one_codepoint") == "a\xff"
assert e.encode("iso-8859-1", "add_one_codepoint") == "\xff"
assert e.encode("utf-16", "add_utf16_bytes") == b'a\xff'
assert e.encode("utf-16-le", "add_utf16_bytes") == b'a\xff'
assert e.encode
