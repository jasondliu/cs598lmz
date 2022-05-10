import codecs
# Test codecs.register_error()

import codecs

def test1():
    buf = codecs.BOM + "abc"
    # This works:
    u1 = buf.decode("utf-16")
    # This works too:
    u2 = codecs.decode(buf, "utf-16")
    assert u1 == u2
    # This works:
    u1 = buf.decode("utf-16", "replace")
    # This fails:
    try:
        u2 = codecs.decode(buf, "utf-16", "replace")
    except UnicodeError:
        #print "test1: OK"
        pass
    else:
        assert 0, "test1: failed"

def test2():
    buf = codecs.BOM + "abc"
    # This works:
    u1 = buf.decode("utf-16", "replace")
    # This works too:
    u2 = codecs.decode(buf, "utf-16", "replace")
    assert u1 == u2
    # This fails:
