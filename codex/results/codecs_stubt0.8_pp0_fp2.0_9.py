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

if not test_support.due_to_ironpython_bug("http://tkbgitvstfat01:8080/WorkItemTracking/WorkItem.aspx?artifactMoniker=30500"):

    def test_encode(encoding):
        u = 'abc'
        b = u.encode(encoding)
        u2 = b.decode(encoding)
        assert u2 == u, (
            "u2.decode(%s)=%s, u=%s" % (encoding, repr(u2), repr(u)))

        u = u'a\u1234'
        b = u.encode(encoding)
        u2 = b.decode(encoding)
        assert u2 == u, (
            "u2.decode(%s)=%s, u=%s" % (encoding, repr(u2), repr(u)))

    def test_encode_error(encoding):
        u = u'a\u123'
        b = u.encode(encoding)
        u2
