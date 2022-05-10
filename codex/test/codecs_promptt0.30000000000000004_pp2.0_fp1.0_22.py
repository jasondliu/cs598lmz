import codecs
# Test codecs.register_error

def test_register_error():
    codecs.register_error("test.lookup", lambda x: (u"\ufffd", x.start + 1))
    s = "abc\x80\x81\x82\x83"
    u = u"abc\ufffd\ufffd\ufffd\ufffd"
    assert codecs.lookup_error("test.lookup")(s) == (u, 5)
    assert codecs.lookup_error("test.lookup")(s, 1) == (u, 2)
    assert codecs.lookup_error("test.lookup")(s, 2) == (u, 3)
    assert codecs.lookup_error("test.lookup")(s, 3) == (u, 4)
    assert codecs.lookup_error("test.lookup")(s, 4) == (u, 5)
    assert codecs.lookup_error("test.lookup")(s, 5) == (u, 5)
