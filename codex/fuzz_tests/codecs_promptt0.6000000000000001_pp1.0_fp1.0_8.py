import codecs
# Test codecs.register_error
import _codecs

# test UTF-16-LE and UTF-16-BE

def test_utf16_le(encoding):
    assert codecs.lookup(encoding).name == encoding
    u = u"\u20ac\u20ac"
    s = u.encode(encoding)
    assert s == b"\xac\x20\xac\x20"
    assert u == s.decode(encoding)
    assert len(s) == 4
    assert len(u) == 2
    assert (s.decode(encoding, "strict") ==
            u.encode(encoding).decode(encoding, "strict") ==
            u)
    assert (s.decode(encoding, "replace") ==
            u.encode(encoding).decode(encoding, "replace") ==
            u"\ufffd\ufffd")
    assert (s.decode(encoding, "ignore") ==
            u.encode(encoding).decode(encoding, "ignore") ==
            u
